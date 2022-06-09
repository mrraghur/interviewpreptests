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
        if l1.length()<0 or l1.length>100:
            print('Please input a list of size between 0 and 100')
            continue
        if n<0 or n>100:
            print('Please input a number between 0 and 100', testcaseNumber)
            continue
    except:
        print('Invalid testcase', testcaseNumber)
        continue
    
    
    obj = Solution()
    ans = obj.solutionGold(l1,n)
    userAns = obj.soluser(l1,n)
    check(ans, userAns, testcaseNumber)

count_cases()

    
