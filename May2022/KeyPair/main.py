from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self,arr,x):
            n=len(arr)
            s = set()
            for i in range(0, n):
                res = x - int(arr[i])
                if res in s:
                    return True 
                s.add(int(arr[i]))
            return False
        def soluser(self, num):
            x = []
            k = -2
            return x

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/kp" + str(j+1) + ".txt") as f:
            #num=int(f.read())
            content =f.readlines()
            num=[x.strip() for x in content]
            #if num.length()<3 or num.length()>1000:
                #print("Please enter an array of size in range of [3,1000]; testcase-",testcaseNumber)
        with open("testcases/kp1" + str(j+1) + ".txt") as f:
            sum=int(f.read())
    except:
        print('Invalid testcase', testcaseNumber)
        continue
     
    obj = Solution()
    ans = obj.solutionGold(num,sum)
    userAns = obj.soluser(num)
    check(ans, userAns, testcaseNumber)

count_cases()