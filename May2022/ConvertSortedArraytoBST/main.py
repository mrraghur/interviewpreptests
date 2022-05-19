import common


n = 10  # number of testcases
CountPassed = 0
CountFailed = 0

class Solution:
        def solutionGold(self, num):
            if not num:
                return None

            mid = len(num) // 2

            root = common.TreeNode(num[mid])
            root.left = self.solutionGold(num[:mid])
            root.right = self.solutionGold(num[mid + 1 :])

            return root

        def soluser(self, nums):
            # wrong solution
            x = []
            k = -2
            return k


for j in range(n):
    try:
        with open("testcases/ArrtoBST" + str(j + 1) + ".txt") as f:
            content = f.readlines()
            arr = [int(x) for x in content]
    except:
        print('Invalid testcase')
    


    obj = Solution()
    ans = obj.solutionGold(arr)
    user_ans = obj.soluser(arr)

    if ans == user_ans:
        CountPassed += 1
        print("Passed, testcase-", j+1)
    else:
        CountFailed += 1
        print("Failed, testcase-", j+1)


common.count_cases(CountPassed, CountFailed)


