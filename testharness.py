import json
import sys
sys.path.insert(1, './workspace/')
import python3workspace

if ((len(sys.argv) != 2) or (sys.argv[1] == "--help")):
    print ("Usage: " + sys.argv[0] + " <nameoftestclasstorun>")

problem_keyword = sys.argv[1]
# problem_keyword = 'pow_x_n'
loc = 'testcases/'+problem_keyword+'.json'
testcases = open(loc,'r')
testcasesJson = json.load(testcases)

allTestcasesPassed = True
print ("Running testcase workspace/python3workspace/" + problem_keyword + ".py")
for testcase in testcasesJson['testcases']:
    userAnswer = getattr(python3workspace,problem_keyword)(testcase['args'])
    
    if (userAnswer != testcase['expected']):
        allTestcasesPassed = False
        print('Wrong Answer, Please check your solution ')
        print("Your Answer: ",userAnswer,"  Expected Answer: ",testcase['expected'])
    else:
        print('Correct Answer')
        print("Your Answer: ",userAnswer,"  Expected Answer: ",testcase['expected'])

if (allTestcasesPassed):
    print ("All testcases passed. Good going.")
else:
    print ("Some testcases failed. Please fix your solution and try again")
    assert allTestcasesPassed

