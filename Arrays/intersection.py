#https://leetcode.com/problems/intersection-of-three-sorted-arrays

from typing import List 
from collections import Counter

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        if not arr1 and not arr2 and not arr3:
            return []
        
        res = []
        intersection={}
        for i in arr1:
            if i in intersection:
                intersection[i] += 1
            else:
                intersection[i]=1
        for i in arr2:
            if i in intersection:
                intersection[i] += 1
            else:
                intersection[i]=1
        for i in arr3:
            if i in intersection:
                intersection[i] += 1
            else:
                intersection[i]=1
        for elem in intersection:
            if intersection[elem] >= 3:
                res.append(elem)
        
        return res
        
        

arr1, arr2, arr3 = [197,418,523,876,1356],  [501,880,1593,1710,1870],  [521,682,1337,1395,1764]
arr1, arr2, arr3 = [1,2,3,4,5],  [1,2,5,7,9],  [1,3,4,5,8]
#Output: [1,5]
print(Solution().arraysIntersection(arr1,arr2,arr3))
        

'''
        L1, L2, L3 = len(arr1), len(arr2), len(arr3)
        i = 0
        c = Counter(arr1)
        c.c
        while i < min(L1, L2, L3):
            if arr1[i] == arr2[i] == arr3[i]:
                res.append(arr1[i])
            i+=1

'''