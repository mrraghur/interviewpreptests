n = 10  # number of testcases
cp=0
cf=0
#You have to input two elements in this problem: a list and an integer.
for j in range(n):
    with open("testcases/re" + str(j+1) + ".txt") as f:
        content =f.readlines()
        l1=[x.strip() for x in content]
    with open("testcases/re" + str(j+1) + str(j+1) + ".txt") as f:
        n=int(f.read())
    #print(s1)
    #print(l1)
    def solutionGold(nums,val):
        count=0
        for i in range(len(nums)):
            nums[i]=int(nums[i])
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count,nums
    ans,al=solutionGold(l1,n)
    def soluser(l,t):
        #wrong solution
        x=[]
        k=2
        return k,x;
    u,ul=soluser(l1,n)
    if ans==u and al==ul:
        cp+=1
        print('YES')
    else:
        cf+=1
        print('NO')
    #print(ans)
print("The number of test cases passed: ",cp)
print("The number of test cases failed: ",cf)
