t=[1,2,3,4,5,6,7,8,9,10]
with open('test1.txt') as f:
    content =f.readlines()
    l1=[x.strip() for x in content]
with open('2.txt') as f:
    content =f.readlines()
    l2=[x.strip() for x in content]
#print(l,len(l))
def solutionGold(li):#this is the code for us that gives correct output for each n every test case
    res=[i for n, i in enumerate(li) if i not in li[:n]]
    return res;
ans=solutionGold(l1)#expected output
def solutionuser(lis):#this would be the user's code
    res=[]
    for i in lis:
        if i not in res:
            res.append(i)
    return res;
u=solutionuser(l1)#output for the user's code
if ans==u:print('yes')
else:print('no')
ans=solutionGold(l2)
u=solutionuser(l2)#output for the user's code
if ans==u:print('yes')
else:print('no')
