from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(nums,val):
            count=0
            for i in range(len(nums)):
                nums[i]=int(nums[i])
                if nums[i] != val:
                    nums[count] = nums[i]
                    count += 1
            return count,nums
        def soluser(l,t):
            x = []
            k = -2
            return k,x;
for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/re" + str(j+1) + ".txt") as f:
            content =f.readlines()
            l1=[x.strip() for x in content]
        with open("testcases/re" + str(j+1) + str(j+1) + ".txt") as f:
            n=int(f.read())
    except:
        print('Invalid testcase', testcaseNumber)
    obj = Solution()
    ans,al = obj.solutionGold(l1,n)
    userAns,ul = obj.soluser(l1,n)
    if ans==u and al==ul:
        countPassed+=1
        print("Passed, testcase-", tescaseNumber)
    else:
        countFailed += 1
        print("Failed, testcase-", tescaseNumber)
print("The number of test cases passed: ", countPassed)
print("The number of test cases failed: ", countFailed)
