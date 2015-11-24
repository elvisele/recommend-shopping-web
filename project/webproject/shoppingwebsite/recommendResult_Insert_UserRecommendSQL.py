'''
将推荐结果插入数据库
'''
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shoppingwebsite.settings')

import django
import codecs
django.setup()

from books.models import UserRecommend

def populate():
	with open('data/result.txt','r') as f:
		k = 1
		c = []
		for a in f.readlines():
			b = a.split('\t')
			userid = b[0]
			d = b[1].strip(']\n').strip('[')
			m = d.split(',')
			temp = []
			for i in m:
				temp.append(i.split(':')[0])
			item = ','.join(temp)
			c.append(UserRecommend(userid=userid,item=item))
			k = k + 1
			print ('transforming ', k, ' line....................................')
	print ('insert sql.....')
	UserRecommend.objects.bulk_create(c)
	print ('already complete ...................')
# Start execution here!
if __name__ == '__main__':
	print ("Starting delete UserRecommend....")
	UserRecommend.objects.all().delete()
	print ("Delete UserRecommend success....")
	print ("Starting insert UserRecommend script...")
	populate()