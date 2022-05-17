n = 10  # number of testcases
cp = 0
cf = 0
for j in range(n):
    with open("Delnode" + str(j + 1) + ".txt") as f:
        content = f.readlines()
        root1 = [x for x in content]
    with open("testcases/Delnode" + str(j + 1) + str(j + 1) + ".txt") as f:
        key1 = int(f.read())

    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

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

    obj = Solution()
    ans = obj.solutionGold(root1, key1)

    def soluser(root, key):
        # wrong solution
        x = []
        k = -2
        return k

    u = soluser(root1, key1)

    if ans == u:
        cp += 1
        print("YES")
    else:
        cf += 1
        print("NO")


print("The number of test cases passed: ", cp)
print("The number of test cases failed: ", cf)
