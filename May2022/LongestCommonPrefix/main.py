n = 10  # number of testcases
cp=0
cf=0
for j in range(n):
    with open("testcases/Lcp" + str(j+1) + ".txt") as f:
    content =f.readlines()
    s1=[x.strip() for x in content]
    #print(s1)
    #print(l1)
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    def solutionGold(s):
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]
        m = len(min(strs, key=len))
        i = 0
        reference = strs[0]
        while i < m:
            for myStr in strs:
                if myStr[i] != reference[i]:
                    return reference[:i]
            i += 1
        return reference[:m]
    ans=solutionGold(s1)
    def soluser(s):
        #wrong solution 
        x=[]
        k=""
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
