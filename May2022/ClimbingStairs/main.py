from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self, n: int) -> int:
            a, b = 0, 1
            for _ in range(n):
                a, b = b, a + b
            return b
        def soluser(self, num):
            x = []
            k = -2
            return k

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/cs" + str(j+1) + ".txt") as f:
            i=int(f.read())
        if i<1 or i>45:
            print("Please input an integer in range of [1, 45]; testcase-", testcaseNumber)

    except:
        print('Invalid testcase', testcaseNumber)
        continue
     
    obj = Solution()
    ans = obj.solutionGold(i)
    userAns = obj.soluser(i)
    check(ans, userAns, testcaseNumber)

count_cases()