from typing import List
import json
from schema import Schema, And, Use, Optional, SchemaError

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1)*int(num2))