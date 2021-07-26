from typing import List
import json
from schema import Schema, And, Use, Optional, SchemaError

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n