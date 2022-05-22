from common import *

n = 10  # number of testcases

class Solution:
        def solutionGold(self, num):
            if not num:
                return None

            mid = len(num) // 2

            root = TreeNode(num[mid])
            root.left = self.solutionGold(num[:mid])
            root.right = self.solutionGold(num[mid + 1 :])

            return root

        def soluser(self, nums):
            # wrong solution
            x = []
            k = -2
            return k


for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/ArrtoBST" + str(j + 1) + ".txt") as f:

            content = f.readlines()
            arr = [int(x) for x in content]
    except:
        print('Invalid testcase')


    

    obj = Solution()
    ans = obj.solutionGold(arr)
    userAns = obj.soluser(arr)
    check(ans, userAns, testcaseNumber)

count_cases()



