print ("starting add shoppinginfo to ratings...")
with open ("data/user-book-ratings.txt",'a+') as f:
	with open("data/info.txt",'r') as f1:
		for a in f1.readlines():
			f.write(a)
print ("delete shoppinginfo...")
with open("data/info.txt",'w') as f2:
	f2.truncate()
print ("already processing success...")