from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self, nums):
            odd=0
            even=0
            for i,item in enumerate(nums):
                if i%2!=0:
                    odd+=int(item)
                else:
                    even+=int(item)
            preveven=0
            prevodd=0
            count=0
            for i, item in enumerate(nums):
                if i%2!=0:
                    if even+prevodd==odd-int(item)+preveven:
                        count+=1
                    odd-=int(item)
                    prevodd+=int(item)
                elif i%2==0:
                    if odd+preveven==even-int(item)+prevodd:
                        count+=1
                    even-=int(item)
                    preveven+=int(item)
            return count
        def soluser(self, nums):
            k=-1
            return k

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("fa" + str(j+1) + ".txt") as f:
            #num=int(f.read())
            content =f.readlines()
            num=[x.strip() for x in content]
            #print(num)
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