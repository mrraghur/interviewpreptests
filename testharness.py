import json
import sys
sys.path.insert(1, './workspace/')
import python3

if ((len(sys.argv) != 2) or (sys.argv[1] == "--help")):
    print ("Usage: " + sys.argv[0] + " <nameoftestclasstorun>")

problem_keyword = sys.argv[1]
loc = 'testcases/'+problem_keyword+'.json'
testcases = open(loc,'r')
testcasesJson = json.load(testcases)

print ("Running testcase workspace/python3/" + problem_keyword + ".py")
for testcase in testcasesJson['testcases']:
    userAnswer = getattr(python3,problem_keyword)(testcase['args'])
    allTestcasesPassed = True;
    try:
        print('Correct Answer')
        print("Your Answer: ",userAnswer,"  Expected Answer: ",testcase['expected'])
    except:
        if (userAnswer != testcase['expected']):
            allTestcasesPassed = false;
            print('Wrong Answer, Please check your solution ')
            print("Your Answer: ",userAnswer,"  Expected Answer: ",testcase['expected'])

    if (allTestcasesPassed):
        print ("All testcases passed. Good going.")
    else:
        print ("Some testcases failed. Please fix your testcases and try again")
        assert allTestcasesPassed
