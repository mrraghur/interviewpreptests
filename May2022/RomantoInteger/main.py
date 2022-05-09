from typing import List
with open('s1.txt') as f:
    s1 =f.read()
    #print(s1)
    #print(l1)
with open('s2.txt') as f:
    s2 =f.read()
with open('s3.txt') as f:
    s3 =f.read()
with open('s4.txt') as f:
    s4 =f.read()
with open('s5.txt') as f:
    s5 =f.read()
with open('s6.txt') as f:
    s6 =f.read()
with open('s7.txt') as f:
    s7 =f.read()
with open('s8.txt') as f:
    s8 =f.read()
with open('s9.txt') as f:
    s9 =f.read()
with open('s10.txt') as f:
    s10 =f.read()
#with open('ms10.txt') as f:
    #content = f.readlines()
    #l10 = [x.strip() for x in content]
#with open('sip11.txt') as f:
    #n=int(f.read())
#print(l1,n)
roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
def solutionGold(S):
    summ = 0
    for i in range(len(S) - 1, -1, -1):
        num = roman[S[i]]
        if 3 * num < summ:
            summ = summ - num
        else:
            summ = summ + num
    return summ
ans=solutionGold(s1)
def soluser(S):#wrong solution
    x=[]
    k=2
    return k;
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
