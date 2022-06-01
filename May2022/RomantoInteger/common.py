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
