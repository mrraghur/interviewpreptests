from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self, num: int) -> List[int]:
            results = [0]
            for i in range(1, num+1):
                results.append(results[i & (i-1)] + 1)
            return results
        def soluser(self, num):
            x = []
            k = -2
            return x

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/Cbits" + str(j+1) + ".txt") as f:
            i=int(f.read())
        
    except:
        print('Invalid testcase', testcaseNumber)
        continue
     
    obj = Solution()
    ans = obj.solutionGold(i)
    userAns = obj.soluser(i)
    check(ans, userAns, testcaseNumber)
    
count_cases()