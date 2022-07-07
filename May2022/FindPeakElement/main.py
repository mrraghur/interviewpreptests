from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self, nums: List[int]) -> int:
            res=[]
            if len(nums)==1:
                return 0
            if int(nums[0])>int(nums[1]):
                res.append(0)
            for i in range(1,len(nums)-1):
                if int(nums[i])>int(nums[i+1]) and int(nums[i])>int(nums[i-1]):
                    res.append(i)
            if int(nums[-1])>int(nums[-2]):
                res.append(len(nums)-1)
            return res[0]
        def soluser(self, num):
            x = []
            k = -2
            return x

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/fp" + str(j+1) + ".txt") as f:
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