n = 10  # number of testcases
cp=0
cf=0
#You have to input two elements in this problem: a list and an integer.
for j in range(n):
    with open("testcases/sip" + str(j+1) + ".txt") as f:
        content =f.readlines()
        l1=[x.strip() for x in content]
    with open("testcases/sip" + str(j+1) + str(j+1) + ".txt") as f:
        n=int(f.read())
    #print(s1)
    #print(l1)
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
    ans=solutionGold(l1,n)
    def soluser(l,t):
        #wrong solution
        x=[]
        k=2
        return k;
    u,ul=soluser(l1,n)
    if ans==u:
        cp+=1
        print('YES')
    else:
        cf+=1
        print('NO')
    #print(ans)
print("The number of test cases passed: ",cp)
print("The number of test cases failed: ",cf)
