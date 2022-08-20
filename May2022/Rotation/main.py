from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def countRotations(self,arr,low,high):
            arr=list(map(int, arr))
            if (high < low): 
                return 0
            if (high == low): 
                return low
            mid = low + (high - low)/2; 
            mid = int(mid)
            if (mid < high and arr[mid+1] < arr[mid]): 
                return (mid+1)
            if (mid > low and arr[mid] < arr[mid - 1]): 
                return mid
            if (arr[high] > arr[mid]): 
                return self.countRotations(arr, low, mid-1);
            return self.countRotations(arr, mid+1, high)
        def solutionGold(self,arr):
            n=len(arr)
            return self.countRotations(arr, 0, n - 1);
        def soluser(self, num):
            x = []
            k = -2
            return k

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/ro" + str(j+1) + ".txt") as f:
            #num=int(f.read())
            content =f.readlines()
            num=[x.strip() for x in content]
            #if num.length()<3 or num.length()>1000:
                #print("Please enter an array of size in range of [3,1000]; testcase-",testcaseNumber)
        #with open("testcases/db1" + str(j+1) + ".txt") as f:
            #su=int(f.read())
    except:
        print('Invalid testcase', testcaseNumber)
        continue
     
    obj = Solution()
    ans = obj.solutionGold(num)
    userAns = obj.soluser(num)
    check(ans, userAns, testcaseNumber)

count_cases()