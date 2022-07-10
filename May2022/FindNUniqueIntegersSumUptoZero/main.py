from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self, n: int) -> List[int]:
            temp = []
            if n%2!=0:
                temp.append(0)
            i = 1
            while (i<=n//2):
                temp.append(i)
                temp.append(-i)
                i += 1
            
            return temp
        def soluser(self, num):
            x = []
            k = -2
            return k

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/fu" + str(j+1) + ".txt") as f:
            num=int(f.read())
            #content =f.readlines()
            #num=[x.strip() for x in content]
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