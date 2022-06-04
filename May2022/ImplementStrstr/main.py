from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self, haystack,needle):
            if needle == '':
                return 0
                length = len(needle)
                for i in range(len(haystack) - length + 1):
                    if haystack[i:i + length] == needle:
                        return i
            return -1
        def soluser(self, haystack,needle):
            x = []
            k = -2
            return k;

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/is" + str(j+1) + ".txt") as f:
            content =f.readlines()
            l1=[x.strip() for x in content]
    except:
        print('Invalid testcase', testcaseNumber)
        continue


    obj = Solution()
    ans= obj.solutionGold(l1[0],l1[1])
    userAns = obj.soluser(l1[0],l1[1])
    check(ans,userAns,testcaseNumber)
count_cases()
