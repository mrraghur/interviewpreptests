from typing import List
from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self, prices: List[int]) -> int:
            max_profit = 0
            min_prices = float("inf")
            for i in range(len(prices)):
                if  prices[i] < min_prices:
                    min_prices = prices[i]
                if (prices[i] - min_prices) > max_profit:
                    max_profit = prices[i] - min_prices
            return max_profit
        def soluser(self, num):
            x = []
            k = -2
            return k

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/bss" + str(j+1) + ".txt") as f:
            content =f.readlines()
            l1=[int(x.strip()) for x in content]
        
    except:
        print('Invalid testcase', testcaseNumber)
        continue
     
    obj = Solution()
    ans = obj.solutionGold(l1)
    userAns = obj.soluser(l1)
    check(ans, userAns, testcaseNumber)

count_cases()