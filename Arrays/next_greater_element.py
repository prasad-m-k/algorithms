#https://leetcode.com/problems/next-greater-element-i/
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        greater={}

        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                greater[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        
        while stack:
            greater[stack.pop()] = -1
        
        res = [] #[0]*len(nums1)
        print(greater)
        #for i in range(len(nums1)):
        for i, num in enumerate(nums1):
            #print(nums1[i])
             res.append(greater[nums1[i]])
        
        return res
    

nums1,nums2 = [4,1,2],  [1,3,4,2]        

print(Solution().nextGreaterElement(nums1, nums2))