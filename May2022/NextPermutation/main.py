from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self, nums: List[int]) -> None:
            n = len(nums)
            ind1 = -1
            for i in range(n - 2, -1, -1): 
                if int(nums[i]) < int(nums[i + 1]):
                    ind1 = i
                    break
            if ind1 >= 0:
                for ind2 in range(n - 1, ind1, -1):  
                    if int(nums[ind1]) < int(nums[ind2]):
                        (nums[ind1])=(nums[ind2])
                        (nums[ind2])=(nums[ind1])
                        break
            i, j = ind1 + 1, n - 1
            while i < j:  
                (nums[i])=(nums[j])
                (nums[j])=(nums[i])
                i, j = i + 1, j - 1
        def soluser(self, num):
            x = []
            k = -2
            return x

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/np" + str(j+1) + ".txt") as f:
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