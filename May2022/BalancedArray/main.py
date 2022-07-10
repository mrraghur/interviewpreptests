from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self,a):
            n=len(a)
            sum1=0
            for i in range(int(n//2)):
                sum1+=int(a[i])
            sum2=0
            for i in range(int(n//2),n):
                sum2+=int(a[i])
            return abs(sum1-sum2)
        
        def soluser(self, num):
            x = []
            k = -2
            return x

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/ba" + str(j+1) + ".txt") as f:
            #num=int(f.read())
            content =f.readlines()
            num=[x.strip() for x in content]
            #if num.length()<3 or num.length()>1000:
                #print("Please enter an array of size in range of [3,1000]; testcase-",testcaseNumber)
        #with open("testcases/ra1" + str(j+1) + ".txt") as f:
            #sum=int(f.read())
    except:
        print('Invalid testcase', testcaseNumber)
        continue
     
    obj = Solution()
    ans = obj.solutionGold(num)
    userAns = obj.soluser(num)
    check(ans, userAns, testcaseNumber)

count_cases()