from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self,A):
            import heapq
            import bisect
            N = len(A)
            if N <= 1:
                return 0
            sortList = []
            result = 0
            for i, v in enumerate(A):
                heapq.heappush(sortList, (v, i))
            x = [] 
            while sortList:  
                v, i = heapq.heappop(sortList)  
                y = bisect.bisect(x, i)
                result += i - y
                bisect.insort(x, i)  
            return result
        def soluser(self, num):
            x = []
            k = -2
            return k

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/ci" + str(j+1) + ".txt") as f:
            #num=int(f.read())
            content =f.readlines()
            num=[x.strip() for x in content]
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