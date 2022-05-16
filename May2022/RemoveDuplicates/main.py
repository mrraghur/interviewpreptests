n = 10  # number of testcases
cp=0
cf=0
for j in range(n):
    with open("testcases/rm" + str(j+1) + ".txt") as f:
        content =f.readlines()
        l1=[x.strip() for x in content]
    def solutionGold(li):
        res=[i for n, i in enumerate(li) if i not in li[:n]]
        return res;
    ans=solutionGold(l1)
    def soluser(l):
        #wrong solution 
        x=["Sndsik"]
        k=2
        return x;
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
