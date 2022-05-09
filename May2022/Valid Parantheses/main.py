from typing import List
with open('vp1.txt') as f:
    s1 =f.read()
    #print(s1)
    #print(l1)
with open('vp2.txt') as f:
    s2 =f.read()
with open('vp3.txt') as f:
    s3 =f.read()
with open('vp4.txt') as f:
    s4 =f.read()
with open('vp5.txt') as f:
    s5 =f.read()
with open('vp6.txt') as f:
    s6 =f.read()
with open('vp7.txt') as f:
    s7 =f.read()
with open('vp8.txt') as f:
    s8 =f.read()
with open('vp9.txt') as f:
    s9 =f.read()
with open('vp10.txt') as f:
    s10 =f.read()
#with open('ms10.txt') as f:
    #content = f.readlines()
    #l10 = [x.strip() for x in content]
#with open('sip11.txt') as f:
    #n=int(f.read())
#print(l1,n)
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
def soluser(s):#wrong solution
    x=[]
    k=2
    return False;
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
