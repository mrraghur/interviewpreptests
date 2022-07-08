from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self,arr,k):
            from collections import deque
            n=len(arr)
            res = []
            d = deque()
            for i in range(k):
                while len(d) and arr[i]>=arr[d[-1]]: 
                    d.pop()
                d.append(i)
            for i in range(k,n):      
                res.append (arr[d[0]])
                while len(d) and d[0]<=i-k:
                    d.popleft()
                while len(d) and arr[i]>=arr[d[-1]]:
                    d.pop()
                d.append(i) 
            res.append (arr[d[0]])
            d.popleft()
            return res
        def soluser(self, num):
            x = []
            k = -2
            return x

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/ipl" + str(j+1) + ".txt") as f:
            #num=int(f.read())
            content =f.readlines()
            num=[x.strip() for x in content]
            #if num.length()<3 or num.length()>1000:
                #print("Please enter an array of size in range of [3,1000]; testcase-",testcaseNumber)
        with open("testcases/ipl1" + str(j+1) + ".txt") as f:
            sum=int(f.read())
    except:
        print('Invalid testcase', testcaseNumber)
        continue
     
    obj = Solution()
    ans = obj.solutionGold(num,sum)
    userAns = obj.soluser(num)
    check(ans, userAns, testcaseNumber)

count_cases()