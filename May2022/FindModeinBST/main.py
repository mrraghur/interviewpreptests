from common import *
from collections import defaultdict

n = 10  # number of testcases


class Solution:
        def solutionGold(self, root):
            self.h = defaultdict(dict)        
            def dfs(node):
                if not node: return
                self.h[node.val] = self.h.get(node.val, 0) + 1     
                dfs(node.left)
                dfs(node.right)
                return
            
            dfs(root)        
            sorted_lst = sorted([[k, v] for k, v in self.h.items()], key=lambda x: (x[1], x[0]), reverse=True)              
            return [k for k, v in self.h.items() if v == sorted_lst[0][1]]

        def soluser(self, root):
            # wrong solution
            x = []
            k = -2
            return k


for j in range(n):
    testcaseNumber = j+1
    try:
        #Input values to build the binary search tree
        with open("testcases/Fmb" + str(j + 1) + ".txt") as f:
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


