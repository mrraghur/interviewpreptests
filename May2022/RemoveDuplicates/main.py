from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(li):
            res=[i for n, i in enumerate(li) if i not in li[:n]]
            return res;
        def soluser(l):
            x = ["Sndisk"]
            k = -2
            return x;
for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/rm" + str(j+1) + ".txt") as f:
            content =f.readlines()
            l1=[x.strip() for x in content]
    except:
        print('Invalid testcase', testcaseNumber)
    obj = Solution()
    ans= obj.solutionGold(l1)
    userAns = obj.soluser(l1)
    check(ans,userAns,testcaseNumber)
count_cases()
