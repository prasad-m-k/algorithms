from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        while (L <= R):
            M = (L + R)//2
            
            if target == nums[M]:
                return M
            elif target < nums[M]:
                R = M - 1
            elif target > nums[M]:
                L = M + 1
        
        return -1
    

nums, target = [-1,0,3,5,9,12],  9

print(Solution().search(nums, target))