from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(nums,target):
            start = 0
            end = len(nums) - 1
            while start + 1 < end:
                mid = start + (end - start) // 2
                if int(nums[mid]) == target:
                    end = mid
                elif int(nums[mid]) < target:
                    start = mid
                else:
                    end = mid
            if int(nums[start]) >= target:
                return start
            if int(nums[end]) >= target:
                return end
            return end + 1
        def soluser(l,t):
            x = []
            k = -2
            return k;
#You have to input two elements in this problem: a list and an integer.
for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/sip" + str(j+1) + ".txt") as f:
            content =f.readlines()
            l1=[x.strip() for x in content]
        with open("testcases/sip" + str(j+1) + str(j+1) + ".txt") as f:
            n=int(f.read())
    except:
        print('Invalid testcase', testcaseNumber)
    obj = Solution()
    ans = obj.solutionGold(l1,n)
    userAns = obj.soluser(l1,n)
    check(ans, userAns, testcaseNumber)
count_cases()
