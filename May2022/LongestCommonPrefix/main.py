from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self, strs):
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
        def soluser(self, strs):
            x = []
            k = ""
            return k;
for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/Lcp" + str(j+1) + ".txt") as f:
            content =f.readlines()
            s1=[x.strip() for x in content]
        if s1.length()<1 or s1.length>200:
            print('Please input a list of size between 1 and 200')
            continue
    except:
        print('Invalid testcase', testcaseNumber)
        continue
    obj = Solution()
    ans= obj.solutionGold(s1)
    userAns = obj.soluser(s1)
    check(ans,userAns,testcaseNumber)
count_cases()
