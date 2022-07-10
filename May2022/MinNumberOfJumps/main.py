from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self,arr):
            n=len(arr)
            if len(arr) <= 1 : 
                return 0 
            if int(arr[0]) == 0 :  
                return -1  
            maxReach = int(arr[0]); 
            step = int(arr[0]); 
            jump = 1;
            
            for i in range(1,len(arr)):
                if  i == len(arr) - 1 : 
                    return jump 
                maxReach = max(maxReach, i+int(arr[i]))
                step-=1; 
                if  step == 0 : 
                    jump+=1 
                    if i>=maxReach : 
                        return -1
                    step = maxReach - i 
  
            return -1
        def soluser(self, num):
            x = []
            k = -2
            return k

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/mj" + str(j+1) + ".txt") as f:
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