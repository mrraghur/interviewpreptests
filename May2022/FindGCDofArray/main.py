from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self, nums: List[int]) -> int:
            nums.sort()
            x = int(nums[0])
            y = int(nums[-1])
        
            if x>y:
                sf = y
            else:
                sf = x
            for i in range(1, sf+1):
                if (x%i==0 and y%i==0):
                    gcd = i

            return gcd
        def soluser(self, num):
            x = []
            k = -2
            return k

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/fu" + str(j+1) + ".txt") as f:
            #num=int(f.read())
            content =f.readlines()
            num=[x.strip() for x in content]
            #if num.length()<3 or num.length()>1000:
                #print("Please enter an array of size in range of [3,1000]; testcase-",testcaseNumber)
        #with open("testcases/ptf1" + str(j+1) + ".txt") as f:
            #sum=int(f.read())
    except:
        print('Invalid testcase', testcaseNumber)
        continue
     
    obj = Solution()
    ans = obj.solutionGold(num)
    userAns = obj.soluser(num)
    check(ans, userAns, testcaseNumber)

count_cases()