'''
从评分文件中获取评价为10的物品ID

读取Del_itemID_not_in_BookinfoSQL.py处理后的文件ratings_itemID_exit_Bookinfo.txt

最后输出到populationitemID.txt

'''


with open('data/populationitemID.txt','w') as f1:
	f1.truncate()

j = 0

with open("data/user-book-ratings.txt",'r') as f:
	with open('data/populationitemID.txt','a+') as f2:
		i = 0
		for a in f.readlines():
			k = a.split(',')[1]
			v = a.split(',')[2]
			if v.strip() == '10':
				f2.write(k+'\n')
				j = j + 1
				print("+++++++++++++++++++find " , j , ' lines+++++++++++++++++++++++++++++++++')
			i = i + 1
			print ("processing " , i , ' lines .......................   ')
with open('data/populationitemID.txt','r+') as f3:
	content = f3.read()
	f3.seek(0,0)
	f3.write(str(j)+'\n'+content)
print ("already success process .")