import json
import sys
sys.path.insert(1, './workspace/')

import python3

problem_keyword = 'rotatearray'

loc = 'testcases/'+problem_keyword+'.json'
testcases = open(loc,'r')
testcasesJson = json.load(testcases)



for testcase in testcasesJson['testcases']:
    userAnswer = getattr(python3,problem_keyword)(testcase['args'])
    print("Your Answer: ",userAnswer,"  Expected Answer: ",testcase['expected'])
    try:
        assert userAnswer == testcase['expected']

        print('Correct Answer')
    except:
        print('Wrong Answer, Please check your solution')