from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self,A):
            N = len(A)
            sum = 0
            for i in range(0, N):
                sum += int(A[i])
            sum2 = 0
    
            for i in range(0, N, +1):
                sum -= int(A[i])
                if sum2 == sum:
                    return (i + 1)
                sum2 += int(A[i])
            
            return -1
        def soluser(self, num):
            x = []
            k = -2
            return k

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/ep" + str(j+1) + ".txt") as f:
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