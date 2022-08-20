from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self,arr):
            arr=list(map(int, arr))
            n=len(arr)
            prev2=0
            prev1=arr[0]
            for i in range(1,n):
                incl =prev2+arr[i]
           
                ans=max(incl,prev1)
                prev2=prev1
                prev1=ans
            return prev1
        def soluser(self, num):
            x = []
            k = -2
            return k

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/ms" + str(j+1) + ".txt") as f:
            #num=int(f.read())
            content =f.readlines()
            num=[x.strip() for x in content]
            #if num.length()<3 or num.length()>1000:
                #print("Please enter an array of size in range of [3,1000]; testcase-",testcaseNumber)
        #with open("testcases/db1" + str(j+1) + ".txt") as f:
            #su=int(f.read())
    except:
        print('Invalid testcase', testcaseNumber)
        continue
     
    obj = Solution()
    ans = obj.solutionGold(num)
    userAns = obj.soluser(num)
    check(ans, userAns, testcaseNumber)

count_cases()