from typing import List
with open('sip1.txt') as f:
    content =f.readlines()
    l1=[x.strip() for x in content]
with open('sip11.txt') as f:
    n=int(f.read())
#print(l1,n)
def solutionGold(nums,target):
    start = 0
    end = len(nums) - 1

    while start + 1 < end:
        mid = start + (end - start) // 2

        if int(nums[mid]) == target:
            end = mid
        elif int(nums[mid]) < target:
            start = mid
        else:
            end = mid

    if int(nums[start]) >= target:
        return start

    if int(nums[end]) >= target:
        return end

    return end + 1
ans=solutionGold(l1,n)
def soluser(l,t):#wrong solution
    x=[]
    k=2
    for i in l:
        if int(i)%2==0:
            x.append(i)
    return k;
u=soluser(l1,n)
if ans==u:print('YES')
else:print('NO')
#print(ans)
