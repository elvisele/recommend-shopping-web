import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shoppingwebsite.settings')

import django
import codecs
django.setup()

from books.models import PuplationRecommend

def populate():
    with open('data/populationitemID.txt','r') as f:
        i = 1
        c = []
        f.readline()
        for line in f.readlines():
            a = line.strip()
            c.append(PuplationRecommend(itemid=a))
            i = i+1
            print ('transforming  ' , i,' line.........................................')
    print ('insert sql ....')
    PuplationRecommend.objects.bulk_create(c)
    print ('already complete................')


if __name__ == '__main__':
    print ("Starting delete PuplationRecommend....")
    PuplationRecommend.objects.all().delete()
    print ("Delete PuplationRecommend success....")
    print ("Starting insert PuplationRecommend script...")
    populate()