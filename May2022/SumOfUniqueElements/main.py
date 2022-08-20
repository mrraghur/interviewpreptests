from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self,nums):
            nums=list(map(int, nums))
            sum=0
            temp={}
            for i in nums:
                if temp.get(i):
                    if temp.get(i)!=2:
                        sum-=i
                        temp[i]=2
                else:
                    sum+=i
                    temp[i]=True
            return sum
        
        def soluser(self, num):
            x = []
            k = -2
            return k

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/so" + str(j+1) + ".txt") as f:
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