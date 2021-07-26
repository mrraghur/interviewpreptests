from typing import List
import json
from schema import Schema, And, Use, Optional, SchemaError

class Solution:
    #One method for each keyword.
    # minimumheighttree
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        try:
            n = Schema(int).validate(n)
            edges = Schema(list).validate(edges)

            if n <= 2:
                return [x for x in range(n)]

            neighbors = [set() for x in range(n)]
            for start, end in edges:
                neighbors[start].add(end)
                neighbors[end].add(start)

            leaves = []
            for i in range(n):
                if len(neighbors[i]) == 1:
                    leaves.append(i)

            remaining_nodes = n
            while remaining_nodes > 2:
                remaining_nodes -= len(leaves)
                temp = []

                for leaf in leaves:
                    for neighbor in neighbors[leaf]:
                        neighbors[neighbor].remove(leaf)
                        if len(neighbors[neighbor]) == 1:
                            temp.append(neighbor)
                leaves = temp

            return leaves
        except :
            return "Check the format of input variables"


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

    # rotatematrix
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)
    
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]

    # palindromepartition
    def partition(self, s):
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s)+1):
            if self.isPal(s[:i]):
                self.dfs(s[i:], path+[s[:i]], res)

    def isPal(self, s):
        return s == s[::-1]
