from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self, price: List[int]) -> int:
            n=len(price)
            profit = [0]*n
            max_price = int(price[n-1])
            for i in range(n-2, 0, -1):
                if int(price[i]) > max_price:
                    max_price = int(price[i])
                profit[i] = max(profit[i+1], max_price - int(price[i]))
            min_price = int(price[0])
            for i in range(1, n):
                if int(price[i]) < min_price:
                    min_price = int(price[i])
                profit[i] = max(profit[i-1], profit[i]+(int(price[i])-min_price))
 
            result = profit[n-1]
            return result

        def soluser(self,num):
            x=[]
            k=2
            return k

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/mp" + str(j+1) + ".txt") as f:
            #num=int(f.read())
            content =f.readlines()
            num=[x.strip() for x in content]
            #if num.length()<3 or num.length()>1000:
                #print("Please enter an array of size in range of [3,1000]; testcase-",testcaseNumber)
        
    except:
        print('Invalid testcase', testcaseNumber)
        continue
     
    obj = Solution()
    ans = obj.solutionGold(num)
    userAns = obj.soluser(num)
    check(ans, userAns, testcaseNumber)

count_cases()