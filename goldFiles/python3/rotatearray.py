from typing import List
import json
from schema import Schema, And, Use, Optional, SchemaError

class Solution:
    # rotatearray
    def reverse(self, nums,start,end):
        while start < end:
            nums[start],nums[end] = nums[end],nums[start]
            start,end = start+1,end-1

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        
        self.reverse(nums,0,n-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,n-1)
        # nums[:] = nums[-k:] + nums[:-k]

