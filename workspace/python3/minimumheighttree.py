from typing import List
import json
from schema import Schema, And, Use, Optional, SchemaError


def minimumheighttree(testcase) -> List[int]:
    n,edges = testcase['n'],testcase['edges']
    try:
        n = Schema(int).validate(n)
        edges = Schema(list).validate(edges)

        #"Write your code here and run with testHarness"
        return []
    except :
        return "Check the format of input variables"



