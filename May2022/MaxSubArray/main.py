from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self, nums):
            dp = []
            dp.append(int(nums[0]))
            current_largest_sum = int(dp[0])
            for i in range(1, len(nums)):
                dp.append(max(int(dp[i - 1]) + int(nums[i]), int(nums[i])))
                if int(dp[i]) > current_largest_sum:
                    current_largest_sum = int(dp[i])
            return current_largest_sum

        def soluser(self, strs):
            x = []
            k = ""
            return k;

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/msa" + str(j+1) + ".txt") as f:
            content =f.readlines()
            s1=[x.strip() for x in content]
    except:
        print('Invalid testcase', testcaseNumber)
        continue

    obj = Solution()
    ans= obj.solutionGold(s1)
    userAns = obj.soluser(s1)
    check(ans,userAns,testcaseNumber)
count_cases()
