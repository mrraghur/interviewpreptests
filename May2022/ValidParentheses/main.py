n = 10  # number of testcases
cp=0
cf=0 
for j in range(n):
    with open("testcases/vp" + str(j+1) + ".txt") as f:
        s1=f.read()
    def solutionGold(s):
        pair = dict(('()', '[]', '{}'))
        st = []
        for x in s:
            if x in '([{':
                st.append(x)
            elif len(st) == 0 or x != pair[st.pop()]:
                return False
        return len(st) == 0
    ans=solutionGold(s1)
    def soluser(s):
        #wrong solution
        x=[]
        k=2
        return False;
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
