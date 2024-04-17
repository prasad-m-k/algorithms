#https://leetcode.com/problems/rotate-array/
#import math
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:]+nums[:-k]
        
#Solution().rotate([-1,-100,3,99], 2)
Solution().rotate([1,2,3,4,5,6,7], 3)
# Solution().rotate([1,2], 3)