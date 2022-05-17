n = 10  # number of testcases
cp = 0
cf = 0
for j in range(n):
    with open("testcases/ArrtoBST" + str(j + 1) + ".txt") as f:
        content = f.readlines()
        arr = [int(x) for x in content]

    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    class Solution:
        def solutionGold(self, num):
            if not num:
                return None

            mid = len(num) // 2

            root = TreeNode(num[mid])
            root.left = self.solutionGold(num[:mid])
            root.right = self.solutionGold(num[mid + 1 :])

            return root

    obj = Solution()
    ans = obj.solutionGold(arr)

    def soluser(nums):
        # wrong solution
        x = []
        k = -2
        return k

    u = soluser(arr)

    if ans == u:
        cp += 1
        print("YES")
    else:
        cf += 1
        print("NO")


print("The number of test cases passed: ", cp)
print("The number of test cases failed: ", cf)
