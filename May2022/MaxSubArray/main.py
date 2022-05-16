n = 10  # number of testcases
cp=0
cf=0
for j in range(n):
    with open("testcases/msa" + str(j+1) + ".txt") as f:
    content =f.readlines()
    l1=[x.strip() for x in content]
    #print(s1)
    #print(l1)
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    def solutionGold(nums):
        dp = []
        dp.append(int(nums[0]))
        #print(dp)
        current_largest_sum = int(dp[0])
        for i in range(1, len(nums)):
            dp.append(max(int(dp[i - 1]) + int(nums[i]), int(nums[i])))
            if int(dp[i]) > current_largest_sum:
                current_largest_sum = int(dp[i])
                #print(dp[i])
        return current_largest_sum
    ans=solutionGold(l1)
    def soluser(l):
        #wrong solution 
        x=[]
        k=2
        return k;
    u=soluser(l1)
    if ans==u:
        cp+=1
        print('YES')
    else:
        cf+=1
        print('NO')
    #print(ans)
print("The number of test cases passed: ",cp)
print("The number of test cases failed: ",cf)
