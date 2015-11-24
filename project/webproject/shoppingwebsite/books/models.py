from django.db import models

'''

图书信息

'''

class Bookinfo(models.Model):
	isbn = models.CharField(max_length=50,primary_key=True)
	book_title = models.CharField(max_length=100)
	book_author = models.CharField(max_length=100)
	yesr_publication = models.CharField(max_length=100)
	publisher = models.CharField(max_length=100)
	def __str__(self):
		return self.book_title

'''

用户信息

'''

class Person(models.Model):
	userid = models.CharField(max_length=50,primary_key=True)
	location = models.CharField(max_length=100)
	age = models.CharField(max_length=20,default='20')
	def __str__(self):
		return self.userid

'''

用户推荐信息

'''

class UserRecommend(models.Model):
	userid = models.CharField(max_length=50,primary_key=True)
	item = models.TextField()
	def __str__(self):
		return self.userid

'''

流行商品

'''

class PuplationRecommend(models.Model):
	itemid = models.CharField(max_length=50)
	def __str__(self):
		return self.itemid

'''

购买清单

'''

class Shoppinginfo(models.Model):
	user = models.ForeignKey(Person)
	books = models.ForeignKey(Bookinfo)
	def __str__(self):
		return self.user

'''

购物车清单

'''

class Shoppingcart(models.Model):
	user = models.ForeignKey(Person)
	books = models.ForeignKey(Bookinfo)
	def __str__(self):
		return self.user
