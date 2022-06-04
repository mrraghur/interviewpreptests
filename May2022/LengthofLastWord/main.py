from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self, s):
            lis = list(s.split(" "))
            return len(lis[-1])


        def soluser(self, s):
            x = []
            k = -2
            return k;

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/Llw" + str(j+1) + ".txt") as f:
            s1=f.read()
    except:
        print('Invalid testcase', testcaseNumber)
        continue


    obj = Solution()
    ans= obj.solutionGold(s1)
    userAns = obj.soluser(s1)
    check(ans,userAns,testcaseNumber)
count_cases()
