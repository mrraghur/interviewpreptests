from typing import List
with open('re1.txt') as f:
    content =f.readlines()
    l1=[x.strip() for x in content]
with open('re11.txt') as f:
    n=int(f.read())
#print(l1,n)
def solutionGold(nums,val):
    count=0
    for i in range(len(nums)):
        nums[i]=int(nums[i])
        if nums[i] != val:
            #print(nums[i],val)
            nums[count] = nums[i]
            #print(count,nums[count])
            count += 1
    return count,nums
ans,al=solutionGold(l1,n)
def soluser(l,t):#wrong solution
    x=[]
    k=2
    for i in l:
        if int(i)%2==0:
            x.append(i)
    return k,x;
u,ul=soluser(l1,n)
if ans==u and al==ul:print('YES')
else:print('NO')
#print(ans,al)
