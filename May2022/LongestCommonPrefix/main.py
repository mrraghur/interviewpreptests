from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(strs):
            if len(strs) == 0:
                return ''
            elif len(strs) == 1:
                return strs[0]
            m = len(min(strs, key=len))
            i = 0
            reference = strs[0]
            while i < m:
                for myStr in strs:
                    if myStr[i] != reference[i]:
                        return reference[:i]
                i += 1
            return reference[:m]
        def soluser(strs):
            x = []
            k = ""
            return k;
for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/Lcp" + str(j+1) + ".txt") as f:
            content =f.readlines()
            s1=[x.strip() for x in content]
    except:
        print('Invalid testcase', testcaseNumber)
    obj = Solution()
    ans= obj.solutionGold(s1)
    userAns = obj.soluser(s1)
    check(ans,userAns,testcaseNumber)
count_cases()
