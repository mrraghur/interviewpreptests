import json
import sys

sys.path.insert(1, './workspace/')
import python3workspace
import jsonschema
from jsonschema import validate

if ((len(sys.argv) != 2) or (sys.argv[1] == "--help")):
    print ("Usage: " + sys.argv[0] + " <nameoftestclasstorun>")

def checkLists(l1,l2):
    l1 = list(map(tuple,l1))
    l2 = list(map(tuple,l2))
    if set(l1) == set(l2):
        return 1    
    return 0

problem_keyword = sys.argv[1]
# problem_keyword = 'rotatearray'
loc = 'testcases/'+problem_keyword+'.json'
testcases = open(loc,'r')
testcasesJson = json.load(testcases)

allTestcasesPassed = True
print ("Running testcase workspace/python3workspace/" + problem_keyword + ".py")
schema = testcasesJson['schema']

for testcase in testcasesJson['testcases']:
    try:
        validate(testcase,schema)
        print("testcase in correct format")
    except jsonschema.exceptions.ValidationError as err:
        print(testcase  )
        raise Exception("Check the testcase format")
        
    userAnswer = getattr(python3workspace,problem_keyword)(testcase['args'])
    
    if "checkUnorderedLists" in testcase['args'].keys() and testcase['args']['checkUnorderedLists'] == True:
        print('check for unordered lists')
        result = checkLists(userAnswer,testcase['expected'])
        if result:
            print('Correct Answer')
            print("Your Answer: ",userAnswer,"  Expected Answer: ",testcase['expected'])        
        else:
            allTestcasesPassed = False
            print('Wrong Answer, Please check your solution ')
            print("Your Answer: ",userAnswer,"  Expected Answer: ",testcase['expected'])    
    else:
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

