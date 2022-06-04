from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self, nums,val):
            count = 0
            for i in range(len(nums)):
                if nums[i] != val:
                    nums[count] = nums[i]
                    count += 1
            return count

        def soluser(self, l,t):
            x = []
            k = -2
            return k


for j in range(n):

    testcaseNumber = j+1
    try:
        with open("testcases/re" + str(j+1) + ".txt") as f:
            content =f.readlines()
            l1=[int(x) for x in content]
        with open("testcases/re" + str(j+1) + str(j+1) + ".txt") as f:
            n=int(f.read())
    except:
        print('Invalid testcase', testcaseNumber)
        continue
    
    
    obj = Solution()
    ans = obj.solutionGold(l1,n)
    userAns = obj.soluser(l1,n)
    check(ans, userAns, testcaseNumber)

count_cases()

    
