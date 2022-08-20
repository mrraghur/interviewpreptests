from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self,num):
            if num==1:
                return 1
            return 0.5
        def soluser(self, num):
            x = []
            k = -2
            return k

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/as" + str(j+1) + ".txt") as f:
            num=int(f.read())
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