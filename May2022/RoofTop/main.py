from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self,a):
            arr=list(map(int, a))
            n=len(a)
            ans=0
            c=0
            for i in range(1,n):
                if(a[i]>a[i-1]):
                    c+=1
                    ans=max(c,ans)
                else:
                    c=0
            return ans
        def soluser(self, num):
            x = []
            k = -2
            return k

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/rt" + str(j+1) + ".txt") as f:
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