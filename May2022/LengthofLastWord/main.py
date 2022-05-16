n = 10  # number of testcases
cp=0
cf=0
for j in range(n):
    with open("testcases/Llw" + str(j+1) + ".txt") as f:
    s1 =f.read()
    #print(s1)
    #print(l1)
    def solutionGold(s):
        lis = list(s.split(" "))
        return len(lis[-1])
    ans=solutionGold(s1)
    def soluser(s):
        #wrong solution 
        x=[]
        k=-2
        return k;
    u=soluser(s1)
    if ans==u:
        cp+=1
        print('YES')
    else:
        cf+=1
        print('NO')
    #print(ans)
print("The number of test cases passed: ",cp)
print("The number of test cases failed: ",cf)
