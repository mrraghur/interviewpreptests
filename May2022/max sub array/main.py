from typing import List
with open('ms1.txt') as f:
    content =f.readlines()
    l1=[x.strip() for x in content]
    #print(l1)
with open('ms2.txt') as f:
    content =f.readlines()
    l2=[x.strip() for x in content]
with open('ms3.txt') as f:
    content =f.readlines()
    l3=[x.strip() for x in content]
with open('ms4.txt') as f:
    content =f.readlines()
    l4=[x.strip() for x in content]
with open('ms5.txt') as f:
    content =f.readlines()
    l5=[x.strip() for x in content]
with open('ms6.txt') as f:
    content =f.readlines()
    l6=[x.strip() for x in content]
with open('ms7.txt') as f:
    content =f.readlines()
    l7=[x.strip() for x in content]
with open('ms8.txt') as f:
    content =f.readlines()
    l8=[x.strip() for x in content]
with open('ms9.txt') as f:
    content =f.readlines()
    l9=[x.strip() for x in content]
with open('ms10.txt') as f:
    content =f.readlines()
    l10=[x.strip() for x in content]
#with open('sip11.txt') as f:
    #n=int(f.read())
#print(l1,n)
def solutionGold(nums):
    dp = []
    dp.append(int(nums[0]))
    print(dp)
    current_largest_sum = int(dp[0])
    for i in range(1, len(nums)):
        dp.append(max(int(dp[i - 1]) + int(nums[i]), int(nums[i])))
        if int(dp[i]) > current_largest_sum:
            current_largest_sum = int(dp[i])
            #print(dp[i])
    return current_largest_sum
ans=solutionGold(l1)
def soluser(l):#wrong solution
    x=[]
    k=2
    for i in l:
        if int(i)%2==0:
            x.append(i)
    return k;
u=soluser(l1)
if ans==u:print('YES')
else:print('NO')
#print(ans)
ans=solutionGold(l2)
if ans==u:print('YES')
else:print('NO')
ans=solutionGold(l3)
if ans==u:print('YES')
else:print('NO')
ans=solutionGold(l4)
if ans==u:print('YES')
else:print('NO')
ans=solutionGold(l5)
if ans==u:print('YES')
else:print('NO')
ans=solutionGold(l6)
if ans==u:print('YES')
else:print('NO')
ans=solutionGold(l7)
if ans==u:print('YES')
else:print('NO')
ans=solutionGold(l8)
if ans==u:print('YES')
else:print('NO')
ans=solutionGold(l9)
if ans==u:print('YES')
else:print('NO')
ans=solutionGold(l10)
if ans==u:print('YES')
else:print('NO')
