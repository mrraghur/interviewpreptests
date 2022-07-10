from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self,n):
            def convert(n):
                if n==0:
                    return 0
                digit=n%10
                if digit==0:
                    digit=5
                return convert(n//10) * 10 + digit
            if n==0:
                return 5
            else:
                return convert(n)
        
        def soluser(self, num):
            x = []
            k = -2
            return x

for j in range(n):
    testcaseNumber = j+1
    try:
        #with open("testcases/kp" + str(j+1) + ".txt") as f:
            #num=int(f.read())
            #content =f.readlines()
            #num=[x.strip() for x in content]
            #if num.length()<3 or num.length()>1000:
                #print("Please enter an array of size in range of [3,1000]; testcase-",testcaseNumber)
        with open("testcases/ra1" + str(j+1) + ".txt") as f:
            sum=int(f.read())
    except:
        print('Invalid testcase', testcaseNumber)
        continue
     
    obj = Solution()
    ans = obj.solutionGold(sum)
    userAns = obj.soluser(sum)
    check(ans, userAns, testcaseNumber)

count_cases()