from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self,A, sum):
            A.sort()
            arr_size=len(A)
            for i in range(0, arr_size-2):
                l = i + 1
                r = arr_size-1 
                while (l < r):
                    if( int(A[i]) + int(A[l]) + int(A[r]) == sum):
                        return True
            
                    elif (int(A[i]) + int(A[l]) + int(A[r]) < sum):
                        l += 1
                    else:
                        r -= 1
            return False
        def soluser(self, num):
            x = []
            k = -2
            return True

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/ts" + str(j+1) + ".txt") as f:
            #num=int(f.read())
            content =f.readlines()
            num=[x.strip() for x in content]
            #if num.length()<3 or num.length()>1000:
                #print("Please enter an array of size in range of [3,1000]; testcase-",testcaseNumber)
        with open("testcases/ts1" + str(j+1) + ".txt") as f:
            sum=int(f.read())
    except:
        print('Invalid testcase', testcaseNumber)
        continue
     
    obj = Solution()
    ans = obj.solutionGold(num,sum)
    userAns = obj.soluser(num)
    check(ans, userAns, testcaseNumber)

count_cases()