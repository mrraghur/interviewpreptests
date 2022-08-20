from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self, height: List[int]) -> int:
            left = 0
            right = len(height) - 1
            ans = 0
            while left < right :
                ans = max(ans, min(int(height[left]), int(height[right])) * (right-left))
                if int(height[left]) > int(height[right]) :
                    right -= 1
                else :
                    left += 1
            return ans
        def soluser(self, num):
            x = []
            k = -2
            return k

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/mw" + str(j+1) + ".txt") as f:
            #num=int(f.read())
            content =f.readlines()
            num=[x.strip() for x in content]
            #if num.length()<3 or num.length()>1000:
                #print("Please enter an array of size in range of [3,1000]; testcase-",testcaseNumber)
        
    except:
        print('Invalid testcase', testcaseNumber)
        continue
     
    obj = Solution()
    ans = obj.solutionGold(num)
    userAns = obj.soluser(num)
    check(ans, userAns, testcaseNumber)

count_cases()