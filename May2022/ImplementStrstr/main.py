from typing import List
with open('is1.txt') as f:
    content =f.readlines()
    l1=[x.strip() for x in content]
    #print(l1)
with open('is2.txt') as f:
    content =f.readlines()
    l2=[x.strip() for x in content]
with open('is3.txt') as f:
    content =f.readlines()
    l3=[x.strip() for x in content]
with open('is4.txt') as f:
    content =f.readlines()
    l4=[x.strip() for x in content]
with open('is5.txt') as f:
    content =f.readlines()
    l5=[x.strip() for x in content]
with open('is6.txt') as f:
    content =f.readlines()
    l6=[x.strip() for x in content]
with open('is7.txt') as f:
    content =f.readlines()
    l7=[x.strip() for x in content]
with open('is8.txt') as f:
    content =f.readlines()
    l8=[x.strip() for x in content]
with open('is9.txt') as f:
    content =f.readlines()
    l9=[x.strip() for x in content]
with open('is10.txt') as f:
    content =f.readlines()
    l10=[x.strip() for x in content]
#with open('sip11.txt') as f:
    #n=int(f.read())
#print(l1,n)
def solutionGold(haystack,needle):
    if needle == '':
        return 0
    length = len(needle)
    for i in range(len(haystack) - length + 1):
        if haystack[i:i + length] == needle:
            return i
    return -1
ans=solutionGold(l1[0],l1[1])
def soluser(haystack,needle):#wrong solution
    x=[]
    k=-2
    return k;
u=soluser(l1[0],l1[1])
if ans==u:print('YES')
else:print('NO')
#print(ans)
ans=solutionGold(l2[0],l2[1])
if ans==u:print('YES')
else:print('NO')
ans=solutionGold(l3[0],l3[1])
if ans==u:print('YES')
else:print('NO')
ans=solutionGold(l4[0],l4[1])
if ans==u:print('YES')
else:print('NO')
ans=solutionGold(l5[0],l5[1])
if ans==u:print('YES')
else:print('NO')
ans=solutionGold(l6[0],l6[1])
if ans==u:print('YES')
else:print('NO')
ans=solutionGold(l7[0],l7[1])
if ans==u:print('YES')
else:print('NO')
ans=solutionGold(l8[0],l8[1])
if ans==u:print('YES')
else:print('NO')
ans=solutionGold(l9[0],l9[1])
if ans==u:print('YES')
else:print('NO')
ans=solutionGold(l10[0],l10[1])
if ans==u:print('YES')
else:print('NO')
