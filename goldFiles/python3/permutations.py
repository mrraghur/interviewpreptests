from typing import List
import json
from schema import Schema, And, Use, Optional, SchemaError

class Solution:
    def permute(self, nums):
        return [[n] + p
                for i, n in enumerate(nums)
                for p in self.permute(nums[:i] + nums[i+1:])] or [[]]