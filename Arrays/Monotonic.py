#https://leetcode.com/problems/monotonic-array/
from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        L = len(nums)
        S = 1
        if L <= 2:
            return True
        mono_inc = mono_dec = False

        while (S < L - 1) and (nums[S - 1] == nums[S]):
            S += 1

        if nums[S - 1] > nums[S]:
            mono_dec = True
        elif nums[S - 1] < nums[S]:
            mono_inc = True
        while S < L:
            if nums[S - 1] < nums[S] and mono_dec:
                return False
            if nums[S - 1] > nums[S] and mono_inc:
                return False
            S += 1
        return True

            



nums = [6,5,4,4]
nums = [1,3,2]
nums = [1,2,2,3]
nums = [2,2,2,1,4,5]
nums = [2,2,2]
print(Solution().isMonotonic(nums))        