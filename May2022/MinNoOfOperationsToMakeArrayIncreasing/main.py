from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self,nums):
            count=0
            nums=list(map(int, nums))
            for i in range(len(nums)-1):
                if nums[i+1]<=nums[i]:
                    count+=nums[i]-nums[i+1]+1
                    nums[i+1]+=nums[i]-nums[i+1]+1
            return count
        
        def soluser(self, num):
            x = []
            k = -2
            return k

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/mo" + str(j+1) + ".txt") as f:
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