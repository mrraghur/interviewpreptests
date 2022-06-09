from binarytree import bst, build


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

countPassed, countFailed = 0, 0


def check(ans,userAns,tescaseNumber):
    global countPassed, countFailed

    if ans == userAns:
        countPassed += 1
        print("Passed, testcase-", tescaseNumber)
    else:
        countFailed += 1
        print("Failed, testcase-", tescaseNumber)
    return countPassed,countFailed


def count_cases():
	
	print("The number of test cases passed: ", countPassed)
	print("The number of test cases failed: ", countFailed)



def build_bst(values):
    root = build(values)
    return root

def read_bst(arr):
    res = []
    for i in arr:
        if i >= str(0):
            res.append(int(i))
        else:
            res.append(None)

    return res





