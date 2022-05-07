with open('ts1.txt') as f:
    content =f.readlines()
    l1=[x.strip() for x in content]
with open('ts11.txt') as f:
    n=int(f.read())
#print(l,len(l))
def solutionGold(l,t):
    values = {}
    for idx, value in enumerate(l):
        value=int(value)
        if t - value in values:
            return [values[t - value], idx]
        else:
            values[value] = idx

ans=solutionGold(l1,n)
def soluser(l,t):#wrong solution
    x=[]
    for i in l:
        if int(i)%2==0:
            x.append(i)
    return x;
u=soluser(l1,n)
if ans==u:print('YES')
else:print('NO')
