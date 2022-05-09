from typing import List
with open('llw1.txt') as f:
    s1 =f.read()
    print(s1)
    #print(l1)
with open('llw2.txt') as f:
    s2 =f.read()
with open('llw3.txt') as f:
    s3 =f.read()
with open('llw4.txt') as f:
    s4 =f.read()
with open('llw5.txt') as f:
    s5 =f.read()
with open('llw6.txt') as f:
    s6 =f.read()
with open('llw7.txt') as f:
    s7 =f.read()
with open('llw8.txt') as f:
    s8 =f.read()
with open('llw9.txt') as f:
    s9 =f.read()
with open('llw10.txt') as f:
    s10 =f.read()
#with open('ms10.txt') as f:
    #content = f.readlines()
    #l10 = [x.strip() for x in content]
#with open('sip11.txt') as f:
    #n=int(f.read())
#print(l1,n)
def solutionGold(s):
    lis = list(s.split(" "))
    return len(lis[-1])
ans=solutionGold(s1)
def soluser(s):#wrong solution
    x=[]
    k=-2
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
