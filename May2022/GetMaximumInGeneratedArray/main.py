from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def getMaximumGenerated(self, n: int) -> int:
            nums=[0,1]
            i=1
            while(len(nums)<=n):
                nums.append(nums[i])
                nums.append(nums[i]+nums[i+1])
                i+=1
            return max(nums[:n+1])
        def soluser(self, num):
            x = []
            k = -2
            return k

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/gm" + str(j+1) + ".txt") as f:
            num=int(f.read())
        if num<0 or num>100:
            print("Please enter an integer in range of [0,100]; testcase-",testcaseNumber)
        
    except:
        print('Invalid testcase', testcaseNumber)
        continue
     
    obj = Solution()
    ans = obj.solutionGold(num)
    userAns = obj.soluser(num)
    check(ans, userAns, testcaseNumber)

count_cases() 