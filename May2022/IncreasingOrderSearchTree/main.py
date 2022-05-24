from common import *


n = 2  # number of testcases


class Solution:
        def solutionGold(self, root):
            if root is None:
                return root
            s = list()
            cur = root
            prev = None
            while True:
                if cur:                
                    s.append(cur)
                    cur = cur.left
                elif s:
                    cur = s.pop()                
                    if not prev:
                        head = cur
                    else:
                        prev.right = cur
                    cur.left = None
                    prev = cur
                    cur = cur.right
                else:
                    break
            return head

        def soluser(self, root):
            # wrong solution
            x = []
            k = -2
            return k


for j in range(n):
    testcaseNumber = j+1
    try:
        #Input values to build the binary search tree
        with open("BuiltbyInterns/interviewpreptests/May2022/MinAbsDifferenceinBST/testcases/Ins" + str(j + 1) + ".txt") as f:
            content = f.readlines()
            inp = [x for x in content]
            root1 = build_bst(inp)

    except:
        print('Invalid testcase')


    obj = Solution()
    ans = obj.solutionGold(root1)
    userAns = obj.soluser(root1)
    check(ans, userAns, testcaseNumber)

count_cases()


