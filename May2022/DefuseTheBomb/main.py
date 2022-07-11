from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self,code,k):
            code=list(map(int, code))
            nums = code+code        
            out = []
            if k == 0:
                return len(code)*[0]
            elif k > 0:
                for i in range(len(code)):
                    out.append(sum(nums[i+1:i+k+1]))
            else:
                for i in range(len(code), 2*len(code)):                
                    out.append(sum(nums[i+k:i]))
            return out
        
        def soluser(self, num):
            x = []
            k = -2
            return k

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/db" + str(j+1) + ".txt") as f:
            #num=int(f.read())
            content =f.readlines()
            num=[x.strip() for x in content]
            #if num.length()<3 or num.length()>1000:
                #print("Please enter an array of size in range of [3,1000]; testcase-",testcaseNumber)
        with open("testcases/db1" + str(j+1) + ".txt") as f:
            su=int(f.read())
    except:
        print('Invalid testcase', testcaseNumber)
        continue
     
    obj = Solution()
    ans = obj.solutionGold(num,su)
    userAns = obj.soluser(num)
    check(ans, userAns, testcaseNumber)

count_cases()