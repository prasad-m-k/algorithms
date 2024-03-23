#https://leetcode.com/problems/median-of-two-sorted-arrays/

import bisect
from typing import List
from time import time

def timer_func(func): 
    # This function shows the execution time of  
    # the function object passed 
    def wrap_func(*args, **kwargs): 
        t1 = time() 
        result = func(*args, **kwargs) 
        t2 = time() 
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s') 
        return result 
    return wrap_func

class Solution:

    @timer_func
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        self.median=0
        self.first=True
        self.sortedarr = []
        
        #This is to speedup insertion
        if len(nums1) >= len(nums2):
            self.sortedarr = nums1
        else:
            self.first=False
            self.sortedarr = nums2
        
        
        if(not self.first):
            for i in nums1:
                bisect.insort(self.sortedarr,i)
        else:
            for i in nums2:
                bisect.insort(self.sortedarr,i)
        
        self.mid=(len(self.sortedarr))//2
        print(f"mid={self.mid}, len1={len(nums1)}, len2={len(nums2)}, nums1={nums1}, nums2={nums2}, self.sortedarr={self.sortedarr}")
        if (len(self.sortedarr) % 2 == 1):
            self.median = self.sortedarr[self.mid]
        else:
            self.median = (self.sortedarr[self.mid-1]+self.sortedarr[self.mid])/2
            
        print (f"median={self.median}")
        return self.median
        

nums1 = [1,3]
nums2 = [2]
nums1 = [1,2]
nums2 = [3,4]
nums1 = []
nums2 = [2,3]
nums1 = []
nums2 = [1,2,3,4,5]


Solution().findMedianSortedArrays(nums1,nums2)