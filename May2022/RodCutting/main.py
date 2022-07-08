from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self,price):
            n=len(price)
            val = [0]*(n+1)
            for i in range(1,n+1):
                max_val = -1
                for j in range(i):
                    max_val = max(max_val, int(price[j]) + val[i - j - 1])
                val[i] = max_val
            return val[n]
        def soluser(self, num):
            x = []
            k = -2
            return k

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/rc" + str(j+1) + ".txt") as f:
            #num=int(f.read())
            content =f.readlines()
            num=[x.strip() for x in content]
            #if num.length()<3 or num.length()>1000:
                #print("Please enter an array of size in range of [3,1000]; testcase-",testcaseNumber)
        #with open("testcases/cc1" + str(j+1) + ".txt") as f:
            #sum=int(f.read())
    except:
        print('Invalid testcase', testcaseNumber)
        continue
     
    obj = Solution()
    ans = obj.solutionGold(num)
    userAns = obj.soluser(num)
    check(ans, userAns, testcaseNumber)

count_cases()