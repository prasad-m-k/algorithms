#https://leetcode.com/problems/search-in-rotated-sorted-array
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums)-1
        
        while (L <= R):
            if nums[L] == target:
                return L
            if nums[R] == target:
                return R
        
            M = (L+R)//2
            if target == nums[M]:
                return M
            elif nums[M] >= nums[L]:
                if target >= nums[L] and target < nums[M]:
                    R = M - 1
                else:
                    L = M + 1
            else:
                if target <= nums[R] and target > nums[M]:
                    L = M + 1
                else:
                    R = M - 1


        return -1
        


nums,target = [4,5,6,7,0,1,2],  3
nums,target = [4,5,6,7,0,1,2],  0

print(Solution().search(nums, target))