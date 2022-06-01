from common import *
n = 10  # number of testcases
roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
class Solution:
        def solutionGold(S):
            summ = 0
            for i in range(len(S) - 1, -1, -1):
                num = roman[S[i]]
                if 3 * num < summ:
                    summ = summ - num
                else:
                    summ = summ + num
            return summ
        def soluser(S):
            x = []
            k = -2
            return k;
for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/rmn" + str(j + 1) + ".txt") as f:
            rmn = f.read()
    except:
        print('Invalid testcase', testcaseNumber)
    obj = Solution()
    ans = obj.solutionGold(rmn)
    userAns = obj.soluser(rmn)
    check(ans, userAns, testcaseNumber)
count_cases()
