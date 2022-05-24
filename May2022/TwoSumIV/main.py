from common import *

n = 10  # number of testcases


class Solution:
        def solutionGold(self, root, k, skip_node):
            if root is None:
                return None
            
            if root.val == k:
                if root == skip_node:
                    return None
                return root
            elif root.val < k:
                return self.findNumber(root.right, k, skip_node)
            else:
                return self.findNumber(root.left, k, skip_node)

        def findTarget(self, root, k):
            queue = [root,]
            while len(queue) > 0:
                node = queue.pop(0)
                if node is not None:
                    if self.findNumber(root, k-node.val, node) is not None:
                        return True
                    queue.append(node.left)
                    queue.append(node.right)
            return False

        def soluser(self, root, k):
            # wrong solution
            x = []
            k = -2
            return False


for j in range(n):
    testcaseNumber = j+1
    try:
        #Input values to build the binary search tree
        with open("testcases/twos" + str(j + 1) + ".txt") as f:
            content = f.readlines()
            inp = [x for x in content]
            root1 = build_bst(inp)
        #Input key which needs to be deleted from binary search tree
        with open("testcases/twos" + str(j + 1) + str(j + 1) + ".txt") as f:
            k = f.read()
    except:
        print('Invalid testcase')


    obj = Solution()
    ans = obj.solutionGold(root1, k)
    userAns = obj.soluser(root1, k)
    check(ans, userAns, testcaseNumber)

count_cases()


