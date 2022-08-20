from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self,arr: list) -> int:
            n=len(arr)
            l = 0
            r = n-1
            while(l <= r):
                mid = (l + r) >> 1
                if((mid == 0 or int(arr[mid - 1]) <= int(arr[mid])) and (mid == n - 1 or int(arr[mid + 1]) <= int(arr[mid]))):
                    break
                if(mid > 0 and int(arr[mid - 1]) > int(arr[mid])):
                    r = mid - 1
                else:
                    l = mid + 1
            return mid
        def soluser(self, num):
            x = []
            k = -2
            return k

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/bp" + str(j+1) + ".txt") as f:
            #num=int(f.read())
            content =f.readlines()
            num=[x.strip() for x in content]
            #if num.length()<3 or num.length()>1000:
                #print("Please enter an array of size in range of [3,1000]; testcase-",testcaseNumber)
        #with open("testcases/cc1" + str(j+1) + ".txt") as f:
            #sum=int(f.read())
    except:
        print('Invalid testcase', testcaseNumber)
        continue
     
    obj = Solution()
    ans = obj.solutionGold(num)
    userAns = obj.soluser(num)
    check(ans, userAns, testcaseNumber)

count_cases()