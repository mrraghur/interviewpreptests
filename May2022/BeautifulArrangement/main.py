from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self,num):
            res=0
            i=num
            def solve(num,i,ans):
                nonlocal res
                if(i==1): 
                    res+=1
                    return res
                for k in range(num,0,-1):
                    if k not in ans:
                        if k%i==0 or i%k==0:
                            ans.append(k)
                            solve(num,i-1,ans)
                            ans.pop()
                return res
            return solve(num,i,[])
        def soluser(self, num):
            x = []
            k = -2
            return k

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/ba" + str(j+1) + ".txt") as f:
            num=int(f.read())
        if num<1 or num>15:
            print("Please enter an integer in range of [1,15]; testcase-",testcaseNumber)
        
    except:
        print('Invalid testcase', testcaseNumber)
        continue
     
    obj = Solution()
    ans = obj.solutionGold(num)
    userAns = obj.soluser(num)
    check(ans, userAns, testcaseNumber)

count_cases()