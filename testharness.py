import sys
import json
import jsonschema
from jsonschema import validate
sys.path.insert(1, './workspace/')
import python3workspace

if ((len(sys.argv) != 2) or (sys.argv[1] == "--help")):
    print ("Usage: python testharness.py <nameoftestclasstorun>")
    quit()

def checkLists(l1,l2):
    # Method to compare two lists if they are unordered
    l1 = list(map(tuple,l1))
    l2 = list(map(tuple,l2))
    if set(l1) == set(l2):
        return 1    
    return 0

problem_keyword = sys.argv[1] 
# problem_keyword is used specifying the program that needs to be run
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
        # Validate the testcase with schema present in json file.
        print("testcase in correct format")
    except jsonschema.exceptions.ValidationError as err:
        print(testcase  )
        raise Exception("Check the testcase format")
        # raise error if the testcase didnot pass validation
    userAnswer = getattr(python3workspace,problem_keyword)(testcase['args'])
    
    if "checkUnorderedLists" in testcase['args'].keys() and testcase['args']['checkUnorderedLists'] == True:
        # If the output of the user solution need not be ordered, then use this to check.
        print('check for unordered lists')
        result = checkLists(userAnswer,testcase['expected'])
    else:
        result =  userAnswer != testcase['expected']

    if result:
        print('Correct Answer')
        print("Your Answer: ",userAnswer,"  Expected Answer: ",testcase['expected'])        
    else:
        allTestcasesPassed = False
        print('Wrong Answer, Please check your solution ')
        print("Your Answer: ",userAnswer,"  Expected Answer: ",testcase['expected'])    

if (allTestcasesPassed):
    print ("All testcases passed. Good going.")
else:
    print ("Some testcases failed. Please fix your solution and try again")
    assert allTestcasesPassed
    # Raise error if all testcases didnot pass

