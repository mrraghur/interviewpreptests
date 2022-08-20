from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self,n,k):
            if n==0:
                return 0
            if n==1:
                return k
            if n==2:
                return k*k
            dp = [0] * (n + 1)
            total = k
            mod = 1000000007
         
            dp[1] = k
            dp[2] = k * k   
         
            for i in range(3,n+1):
                dp[i] = ((k - 1) * (dp[i - 1] + dp[i - 2])) % mod
             
            return dp[n]
        def soluser(self, num):
            x = []
            k = -2
            return k

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/ptf" + str(j+1) + ".txt") as f:
            num=int(f.read())
            #content =f.readlines()
            #num=[x.strip() for x in content]
            #if num.length()<3 or num.length()>1000:
                #print("Please enter an array of size in range of [3,1000]; testcase-",testcaseNumber)
        with open("testcases/ptf1" + str(j+1) + ".txt") as f:
            sum=int(f.read())
    except:
        print('Invalid testcase', testcaseNumber)
        continue
     
    obj = Solution()
    ans = obj.solutionGold(num,sum)
    userAns = obj.soluser(num)
    check(ans, userAns, testcaseNumber)

count_cases()