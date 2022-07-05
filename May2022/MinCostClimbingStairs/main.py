from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self, cost: List[int]) -> int:
            dp = [0]*(len(cost))
            dp[-1] = cost[-1]
            dp[-2] = cost[-2]
            for i in range(len(cost)-3,-1,-1):
                dp[i] = min(dp[i+1],dp[i+2])+cost[i]
            return min(dp[0],dp[1])
        def soluser(self, num):
            x = []
            k = -2
            return k

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/mc" + str(j+1) + ".txt") as f:
            #num=int(f.read())
            content =f.readlines()
            num=[x.strip() for x in content]
        #if num<1 or num>15:
            #print("Please enter an integer in range of [1,15]; testcase-",testcaseNumber)
        
    except:
        print('Invalid testcase', testcaseNumber)
        continue
     
    obj = Solution()
    ans = obj.solutionGold(num)
    userAns = obj.soluser(num)
    check(ans, userAns, testcaseNumber)

count_cases()