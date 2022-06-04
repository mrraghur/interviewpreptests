from common import *
n = 10  # number of testcases
from math import factorial
class Solution:
        def solutionGold(self, n):
            catalan_number = factorial(2 * n) // factorial(n) // factorial(n) // (n + 1)
            return catalan_number
        def soluser(self, n):
            x = []
            k = -2
            return k

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/UnqBST" + str(j + 1) + ".txt") as f:
            n = int(f.read())
        if n<1 or n>19:
            print('Please input a number between 1 and 19', testcaseNumber)
            continue
    except:
        print('Invalid testcase', testcaseNumber)
        continue



    obj = Solution()
    ans = obj.solutionGold(n)
    userAns = obj.soluser(n)
    check(ans, userAns, testcaseNumber)
count_cases()
