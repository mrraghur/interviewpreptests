from common import *


n = 2  # number of testcases


class Solution:
        def solutionGold(self, root):
            def fn(node, lo, hi):
                if not node: return hi - lo
                left = fn(node.left, lo, node.val)
                right = fn(node.right, node.val, hi)
                return min(left, right)
            return fn(root, float('-inf'), float('inf'))

        def soluser(self, root):
            # wrong solution
            x = []
            k = -2
            return k


for j in range(n):
    testcaseNumber = j+1
    try:
        #Input values to build the binary search tree
        with open("BuiltbyInterns/interviewpreptests/May2022/MinAbsDifferenceinBST/testcases/Minabs" + str(j + 1) + ".txt") as f:
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


