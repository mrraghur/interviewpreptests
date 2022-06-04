from common import *

n = 10  # number of testcases


class Solution:
        def solutionGold(self, root, key):
            if not root:
                return None

            if root.val == key:
                if not root.right:
                    return root.left

                if not root.left:
                    return root.right

                if root.left and root.right:
                    temp = root.right
                    while temp.left:
                        temp = temp.left
                    root.val = temp.val
                    root.right = self.solutionGold(root.right, root.val)

            elif root.val > key:
                root.left = self.solutionGold(root.left, key)
            else:
                root.right = self.solutionGold(root.right, key)

            return root

        def soluser(self, root, key):
            # wrong solution
            x = []
            k = -2
                    


for j in range(n):
    testcaseNumber = j+1
    try:
        #Input values to build the binary search tree
        with open("testcases/Delnode" + str(j + 1) + ".txt") as f:
            content = f.readlines()
            inp = [x for x in content]
            root1 = build_bst(inp)
        #Input key which needs to be deleted from binary search tree
        with open("testcases/Delnode" + str(j + 1) + str(j + 1) + ".txt") as f:
            key1 = f.read()
    except:
        print('Invalid testcase', testcaseNumber)
        continue


    obj = Solution()
    ans = obj.solutionGold(root1, key1)
    userAns = obj.soluser(root1, key1)
    check(ans, userAns, testcaseNumber)

count_cases()


