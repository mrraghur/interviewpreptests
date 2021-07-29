import json
import random,string
import numpy as np
import sys 
problem_keyword = sys.argv[1] 
# problem_keyword is used specifying the program that needs to be run
# problem_keyword = 'permutations'

def genArgUsingDtype(d,type):
    # Read the datatype and generate random testcase
    length = random.randint(3,50)
    if d == "string":
        return ''.join(random.choice(string.ascii_letters) for m in range(length))
    elif d == "integer":
        return random.randint(0,50)
    elif d == "array":
        if type['items']['type'] == 'number':
            return list(np.random.randint(-50,50,random.randint(1,50)))
    elif d == "number":
        return random.random()*random.randint(-100,100)


testcases = open(f'./testcases/{problem_keyword}.json')
testcases = json.load(testcases)
# print(testcases)


inputArgs = list(testcases['testcases'][0]['args'].keys())
schema = testcases['schema']
args = testcases['testcases'][0]['args'].copy()
print(inputArgs)
if 'checkUnorderedLists' in inputArgs:
    inputArgs.remove('checkUnorderedLists')
for i in inputArgs:
    dtype = schema['properties']['args']['properties'][i]['type']
    arg = genArgUsingDtype(dtype,schema['properties']['args']['properties'][i])
    args[i] = arg

# print(dtype)
print(args)
