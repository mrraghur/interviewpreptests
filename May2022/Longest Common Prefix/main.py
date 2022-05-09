from typing import List
with open('lcp1.txt') as f:
    content =f.readlines()
    s1=[x.strip() for x in content]
    #print(s1)
    #print(l1)
with open('lcp2.txt') as f:
    s2 =f.readline()
with open('lcp3.txt') as f:
    s3 =f.readlines()
with open('lcp4.txt') as f:
    s4 =f.readlines()
with open('lcp5.txt') as f:
    s5 =f.readlines()
with open('lcp6.txt') as f:
    s6 =f.readlines()
with open('lcp7.txt') as f:
    s7 =f.readlines()
with open('lcp8.txt') as f:
    s8 =f.readlines()
with open('lcp9.txt') as f:
    s9 =f.readlines()
with open('lcp10.txt') as f:
    s10 =f.readlines()
#with open('ms10.txt') as f:
    #content = f.readlines()
    #l10 = [x.strip() for x in content]
#with open('sip11.txt') as f:
    #n=int(f.read())
#print(l1,n)
roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
def solutionGold(strs):
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
def soluser(strs):#wrong solution
    x=[]
    k=2
    s=""
    return s;
u=soluser(s1)
if ans==u:print('YES')
else:print('NO')
#print(ans)
ans=solutionGold(s2)
if ans==u:print('YES')
else:print('NO')
ans=solutionGold(s3)
if ans==u:print('YES')
else:print('NO')
ans=solutionGold(s4)
if ans==u:print('YES')
else:print('NO')
ans=solutionGold(s5)
if ans==u:print('YES')
else:print('NO')
ans=solutionGold(s6)
if ans==u:print('YES')
else:print('NO')
ans=solutionGold(s7)
if ans==u:print('YES')
else:print('NO')
ans=solutionGold(s8)
if ans==u:print('YES')
else:print('NO')
ans=solutionGold(s9)
if ans==u:print('YES')
else:print('NO')
ans=solutionGold(s10)
if ans==u:print('YES')
else:print('NO')
