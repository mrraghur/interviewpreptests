from cgi import print_arguments
from common import *

n = 10  # number of testcases


class Solution:
        def solutionGold(self, root, k):
            def dfs(root, seen):
                if root == None: return False
                complement = k - root.val
                if complement in seen: return True
                seen.add(root.val)
                return dfs(root.left, seen) or dfs(root.right, seen)
        
            return dfs(root, set())

        def soluser(self, root, k):
            # wrong solution
            x = []
            k = -2
            return False


for j in range(2):
    testcaseNumber = j+1
    try:
        #Input values to build the binary search tree
        with open("testcases/twos" + str(j + 1) + ".txt") as f:
            content = f.readlines()

            inp = read_bst(content)
 
            root1 = build_bst(inp)
        #Input key which needs to be deleted from binary search tree
        with open("testcases/twos" + str(j + 1) + str(j + 1) + ".txt") as f:
            k = int(f.read())
    except:
        print('Invalid testcase')


    obj = Solution()
    ans = obj.solutionGold(root1, k)
    userAns = obj.soluser(root1, k)
    check(ans, userAns, testcaseNumber)

count_cases()


