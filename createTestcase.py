import json
import random,string
import numpy as np
import sys 
problem_keyword = sys.argv[1] 
# problem_keyword is used specifying the program that needs to be run
# problem_keyword = 'permutations'

def genArgUsingDtype(d,type):
    # Read the datatype and generate random testcase
    if d == "string": # generate a random string of length between 3 and 50 
        length = random.randint(3,50)
        return ''.join(random.choice(string.ascii_letters) for m in range(length))
    elif d == "integer": # integer numbers
        return random.randint(0,50)
    elif d == "array": 
        if type['items']['type'] == 'number': # generate a random array
            return list(np.random.randint(-50,50,random.randint(1,50)))
    elif d == "number": #float numbers
        return random.random()*random.randint(-100,100)
    elif d == "matrix": # generate a square matrix of size matrixSize
        matrixSize = random.randint(1,15)
        return np.random.randint(0,2,(matrixSize,matrixSize))

testcases = open(f'./testcases/{problem_keyword}.json')
testcases = json.load(testcases)
# print(testcases)


inputArgs = list(testcases['testcases'][0]['args'].keys())
schema = testcases['schema']
args = testcases['testcases'][0]['args'].copy()

if 'checkUnorderedLists' in inputArgs:
    inputArgs.remove('checkUnorderedLists')
for i in inputArgs: 
    """
    pass all the input args types to the generator 
    function and get random testcase for input argument
    """
    dtype = schema['properties']['args']['properties'][i]['type']
    arg = genArgUsingDtype(dtype,schema['properties']['args']['properties'][i])
    args[i] = arg

print(args)