from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(l,t):
            values = {}
            for idx, value in enumerate(l):
                value=int(value)
                if t - value in values:
                    return [values[t - value], idx]
                else:
                    values[value] = idx
        def soluser(l,t):
            x = []
            k = -2
            for i in l:
                if int(i)%2==0:
                    x.append(i)
            return x;
#You have to input two elements in this problem: a list and an integer.
for j in range(n):
    testcaseNumber = j+1
    try:
        if j==0:
            with open("testcases/ts" + str(j+1) + ".txt") as f:
                content =f.readlines()
                l1=[x.strip() for x in content]
            with open("testcases/ts" + str(j+1) + str(j+1) + ".txt") as f:
                n=int(f.read())
        else:
            with open("testcases/ts" + str(j+1) + ".txt") as f:
                content =f.readlines()
                l1=[x.strip() for x in content]
            with open("testcases/tss" + str(j+1) + ".txt") as f:
                n=int(f.read())
    except:
        print('Invalid testcase', testcaseNumber)
    obj = Solution()
    ans = obj.solutionGold(l1,n)
    userAns = obj.soluser(l1,n)
    check(ans, userAns, testcaseNumber)
count_cases()
