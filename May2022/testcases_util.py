import random
from itertools import combinations, permutations 

n = 10 #how many number of files you want to create


for i in range(10):
	#change the name of file from temp to anything
	f = open("filename" + str(i+1) + ".txt", "w")

	#change the range according to question
	arr = random.sample(range(-10000, 10000), 100 *(i+5))
	#syntax of random.sample is (range(low, high), number of elements)

	#arr.sort()
	#uncomment the above line if you want sorted inputs
	
	for i in arr:
	 	f.write('%d\n' % i)
	
	#f.write("%s" % temp4[i])

	f.close()











