from common import *
n = 10  # number of testcases
class Solution:
        def solutionGold(self, nums):
            x = 1
            for i in range(len(nums)-1):
                if(nums[i]!=nums[i+1]):
                    nums[x] = nums[i+1]
                    x+=1
            return(x)

        def soluser(self, l):
            x = ["Sndisk"]
            k = -2
            return x;

for j in range(n):
    testcaseNumber = j+1
    try:
        with open("testcases/rm" + str(j+1) + ".txt") as f:
            content =f.readlines()
            l1=[x.strip() for x in content]
    except:
        print('Invalid testcase', testcaseNumber)
        continue


    obj = Solution()
    ans= obj.solutionGold(l1)
    userAns = obj.soluser(l1)
    check(ans,userAns,testcaseNumber)
count_cases()
