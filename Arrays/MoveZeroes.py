#https://leetcode.com/problems/move-zeroes/description/

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = right =0
        
        while (right < len(nums)):
            if nums[right] != 0:
                nums[left],nums[right]=nums[right], nums[left]
                left += 1
            right += 1
        
        return nums
        

nums = [0,1,0,3,12]
#print(nums, end = " -> ")
#nums = [0]
print(nums)
print(Solution().moveZeroes(nums))