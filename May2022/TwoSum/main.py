n = 10  # number of testcases
cp=0
cf=0
#You have to input two elements in this problem: a list and an integer.
for j in range(n):
    if j==0:
        with open("testcases/ts" + str(j+1) + ".txt") as f:
            content =f.readlines()
            l1=[x.strip() for x in content]
        with open("testcases/ts" + str(j+1) + str(j+1) + ".txt") as f:
            n=int(f.read())
    else:
        with open("testcases/ts" + str(j+1) + ".txt") as f:
            content =f.readlines()
            l1=[x.strip() for x in content]
        with open("testcases/tss" + str(j+1) + ".txt") as f:
            n=int(f.read())
    #print(s1)
    #print(l1)
    def solutionGold(l,t):
        values = {}
        for idx, value in enumerate(l):
            value=int(value)
            if t - value in values:
                return [values[t - value], idx]
            else:
                values[value] = idx
    ans=solutionGold(l1,n)
    def soluser(l,t):
        #wrong solution
        x=[]
        k=2
        for i in l:
            if int(i)%2==0:
                x.append(i)
        return x;
    u=soluser(l1,n)
    if ans==u:
        cp+=1
        print('YES')
    else:
        cf+=1
        print('NO')
    #print(ans)
print("The number of test cases passed: ",cp)
print("The number of test cases failed: ",cf)
