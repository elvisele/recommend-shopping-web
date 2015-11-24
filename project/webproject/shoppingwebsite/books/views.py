import random
from books.models import *
from books.forms import PersonForm
from django.shortcuts import render
from py4j.java_gateway import JavaGateway
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

'''

python 通过py4j 来调用java

'''

gateway = JavaGateway()
app = gateway.entry_point
recommend = app.prepdata() #prepdata()是java里面的一个方法，装载数据，计算相似度，在这里调用

'''

调用java里的推荐方法，推荐与itemid相似的物品

'''

def getresult(itemid):
	result = app.itemrecommend(itemid,recommend)
	return result

'''

登陆视图

'''

def user_login(request):
	if request.method == 'POST':
		userid = request.POST.get('userid')
		user = Person.objects.filter(userid=str(userid))
		if user:
			request.session['userid'] = str(userid)
			return HttpResponseRedirect('/books/')
		else:
			print ('Invalid login details: {0}'.format(userid))
			return HttpResponse('Invalid login details supplied.')
	else:
		return render(request,'books/login.html',{})

'''

全部商品展示视图

通过随机数来获取数据库的部分值

'''

def listing(request):
	userid = request.session['userid']
	a =  random.randint(1,100000)
	books_list = Bookinfo.objects.all()[a:]
	paginator = Paginator(books_list, 21) # 展示21个商品每页
	page = request.GET.get('page')
	try:
		books = paginator.page(page)
	except PageNotAnInteger:
		books = paginator.page(1)
	except EmptyPage:
		books = paginator.page(paginator.num_pages)
	return render(request,'books/listing.html',{'books':books,'userid':userid})

'''

主页视图 

'''

def index(request):
	if request.session.get('userid'):
		userid = request.session['userid']
	else:
		userid = ''
	a =  random.randint(1,150000) + 1
	b = a+20
	recommenddict=URecommend(userid)
	books_list = Bookinfo.objects.all()[a:b]
	return render(request,'books/index.html',{'books':books_list,'UserRecommenddict':recommenddict,'userid':userid})

'''

注册视图

'''

def register(request):
	registered = False
	if request.method == 'POST':
		print ("ok1")
		person_form = PersonForm(data=request.POST)
		if person_form.is_valid() :
			person = person_form.save(commit=False)
			person.save()
			registered = True
		else:
			print (person_form.errors)
	else:
		person_form = PersonForm()
	return render(request,'books/register.html',
		{'person_form':person_form,'registered':registered})


'''

登陆视图

'''

def user_logout(request):
	request.session['userid'] = ''
	return HttpResponseRedirect('/books/')

'''

得到n个不同的随机数

'''

def randompop(n):
	a = []
	i = 1
	while i <= n:
		mark = 1
		b = random.randint(1,65059)
		for j in a:
			if j == b:
				mark = 0
				break;
		if mark == 1:
			i = i + 1
			a.append(b)
	return a

'''

读取流行的商品

'''

def showpop(n):
	popitem = []
	popitem = randompop(n)
	itemid = []
	books = []
	for v in popitem:
		a = PuplationRecommend.objects.get(id=v)
		itemid.append(a.itemid)
	for k in itemid:
		b = Bookinfo.objects.get(isbn=str(k))
		books.append(b)
	return books

'''

商品详细页面视图

'''

def detail(request,isbn):
	if request.session.get('userid'):
		userid = request.session['userid']
	else:
		userid = ''
	#userid = request.session['userid']
	result = getresult(itemid=int(isbn))
	reason = []
	recommendbooks = []
	for v in result:
		try:
			temp = Bookinfo.objects.get(isbn=str(v))
			recommendbooks.append(temp)
			reason.append(0)
		except Exception:
			pass
	judge(recommendbooks,reason)
	recommenddict=changedict(recommendbooks,reason)
	context_dict = {}
	bookinfo = Bookinfo.objects.get(isbn=isbn)
	context_dict['bookinfo'] = bookinfo
	context_dict['recommenddict'] = recommenddict
	context_dict['userid']=userid
	return render(request,'books/detail.html',context_dict)

'''

进行用户个性化推荐

'''

def URecommend(userid):
	books = []
	reason = []
	recommenddict = {}
	try:
		re = UserRecommend.objects.get(pk=str(userid))
		items = re.item.split(',')
		for i in items:
			temp = Bookinfo.objects.get(isbn=str(i))
			books.append(temp)
			reason.append(0)
	except Exception:
		pass
	finally:
		reason=judge(books,reason)
		recommenddict=changedict(books,reason)
		return recommenddict

'''

判断用户推荐和物品推荐是否够10个，不够同时添加流行推荐

'''	

def judge(a,v):
	if len(a) is 0:
		v = [1]*10
		b=showpop(10)
		for k in b:
			a.append(k)
	elif len(a) < 10:
		c = 10 - len(a)
		books = showpop(c)
		for i in books:
			a.append(i)
			v.append(1)
	else:
		pass
	return v

'''

将推荐商品列表和推荐理由转换为字典

'''

def changedict(a,b):
	c = zip(a,b)
	return dict((k,v) for k,v in c)


'''

将商品加入购物车

'''

def cart(request,isbn):
	if request.session.get('userid'):
		writeinfo(request,isbn,value='5')
		userid = request.session['userid']
		user = Person.objects.get(pk=userid)
		books = Bookinfo.objects.get(pk=isbn)
		shoppingcart = Shoppingcart(user=user,books=books)
		shoppingcart.save()
		return render(request,'books/cart.html',{"userid":userid})
	else:
		return HttpResponseRedirect('/books/login/')
	

'''

购买商品

'''

def buy(request,isbn):
	if request.session.get('userid'):
		writeinfo(request,isbn,value='10')
		userid = request.session['userid']
		user = Person.objects.get(pk=userid)
		books = Bookinfo.objects.get(pk=isbn)
		shoppingcart = Shoppinginfo(user=user,books=books)
		shoppingcart.save()
		return render(request,'books/buy.html',{"userid":userid})
	else:
		return HttpResponseRedirect('/books/login/')

'''

展示购物清单

'''

def shoppingbuy(request):
	userid = request.session['userid']
	user = Person.objects.get(pk=userid)
	books = Shoppinginfo.objects.filter(user=user)
	return render(request,'books/listing_buy.html',{"buybooks":books,"userid":userid})

'''

展示购物车

'''

def shoppingcart(request):
	userid = request.session['userid']
	user = Person.objects.get(pk=userid)
	books = Shoppingcart.objects.filter(user=user)
	for book in books:
		print (book.books.book_title)
	return render(request,'books/listing_cart.html',{"cartbooks":books,"userid":userid})

'''

删除购物车里的商品信息

'''

def deletecart(request,isbn):
	userid = request.session['userid']
	user = Person.objects.get(pk=userid)
	books = Bookinfo.objects.get(pk=isbn)
	Shoppingcart.objects.filter(user=user,books=books).delete()
	writeinfo(request,isbn,value='3')
	return render(request,'books/delcart.html',{"userid":userid})

'''

删除已购买的商品信息

'''

def deleteshopping(request,isbn):
	userid = request.session['userid']
	user = Person.objects.get(pk=userid)
	books = Bookinfo.objects.get(pk=isbn)
	Shoppinginfo.objects.filter(user=user,books=books).delete()
	return render(request,'books/delshopping.html',{"userid":userid})

'''

记录购物行为

'''

def writeinfo(request,isbn,value):
	if request.session.get('userid') == None:
		return
	text = str(request.session.get('userid'))+','+ str(isbn)+','+value
	with open('data/info.txt','a+') as f:
		f.write(text+'\n')

