from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self,a,k):
            import heapq
            arr=list(map(int, a))
            n=len(a)
            min_heap = []
            ans = []
    
            for num in a:
            
                if len(min_heap)<2*k :
                    heapq.heappush(min_heap,num)
                
                else:
                    ans.append(heapq.heappop(min_heap))
                    heapq.heappush(min_heap,num)
    
            while(len(min_heap)):
                ans.append(heapq.heappop(min_heap))
    
            return ans
        def soluser(self, num):
            x = []
            k = -2
            return x

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/ns" + str(j+1) + ".txt") as f:
            #num=int(f.read())
            content =f.readlines()
            num=[x.strip() for x in content]
            #if num.length()<3 or num.length()>1000:
                #print("Please enter an array of size in range of [3,1000]; testcase-",testcaseNumber)
        with open("testcases/ns1" + str(j+1) + ".txt") as f:
            su=int(f.read())
    except:
        print('Invalid testcase', testcaseNumber)
        continue
     
    obj = Solution()
    ans = obj.solutionGold(num,su)
    userAns = obj.soluser(num)
    check(ans, userAns, testcaseNumber)

count_cases()