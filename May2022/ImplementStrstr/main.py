n = 10  # number of testcases
cp=0
cf=0
for j in range(n):
    with open("testcases/is" + str(j+1) + ".txt") as f:
    content =f.readlines()
    l1=[x.strip() for x in content]
    #print(l1)

    def solutionGold(haystack,needle):
    if needle == '':
        return 0
    length = len(needle)
    for i in range(len(haystack) - length + 1):
        if haystack[i:i + length] == needle:
            return i
    return -1
    ans=solutionGold(l1[0],l1[1])
    def soluser(haystack,needle):
        #wrong solution
        x=[]
        k=-2
        return k;
    u=soluser(l1[0],l1[1])
    if ans==u:
        cp+=1
        print('YES')
    else:
        cf+=1
        print('NO')
    #print(ans)
print("The number of test cases passed: ",cp)
print("The number of test cases failed: ",cf)
