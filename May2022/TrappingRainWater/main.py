from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self,arr):
            n = len(arr)
            left = [0]*n
            right = [0]*n
            water = 0
            left[0] = int(arr[0]) 
            for i in range( 1, n): 
                left[i] = max(left[i-1], int(arr[i]))
            right[n-1] = int(arr[n-1]) 
            for i in range(n-2, -1, -1): 
                right[i] = max(right[i+1], int(arr[i]));
            for i in range(0, n): 
                water += min(left[i],right[i]) - int(arr[i])
            return water
        def soluser(self, num):
            x = []
            k = -2
            return k

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/trw" + str(j+1) + ".txt") as f:
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