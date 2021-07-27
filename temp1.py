l1 = [[1,2,4],[1,3,2],[2,1,3]]
l2 = [[2,1,3],[1,2,3],[1,3,2]]



def checkLists(l1,l2):
    a = 1
    if len(l1) == len(l2):
        a *= 1
    else:
        return 0

    for i in l1:
        if i in l2:
            a *= 1
        else:
            return 0
    
    return 1

a = checkLists(l1,l2)
print(a)
