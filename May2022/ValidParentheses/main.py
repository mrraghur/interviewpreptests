from common import *


n = 10  # number of testcases


class Solution:
        def solutionGold(self, s):
            pair = dict(('()', '[]', '{}'))
            st = []
            for x in s:
                if x in '([{':
                    st.append(x)
                elif len(st) == 0 or x != pair[st.pop()]:
                    return False
            return len(st) == 0

        def soluser(self, s):
            # wrong solution
            x = []
            k = -2
            return k


for j in range(n):
    testcaseNumber = j+1
    try:
        #Input values to build the binary search tree
        with open("testcases/vp" + str(j + 1) + ".txt") as f:
            inp = f.read()

    except:
        print('Invalid testcase', testcaseNumber)


    obj = Solution()
    ans = obj.solutionGold(inp)
    userAns = obj.soluser(inp)
    check(ans, userAns, testcaseNumber)

count_cases()


