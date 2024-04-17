from typing import List

class Solution:
    
    def removeDuplicates(self, nums: List[int]) -> int:
        #print(nums)
        L = 1
        for i in range(1, len(nums)):
            if nums[i-1] != nums[ i ]:
                nums[L] = nums[i]
                L += 1
        #print(nums[0:L])
        return L
    
    def removeDuplicates1(self, nums: List[int]) -> int:
        l = 1
        for r in range(l, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        
        print(l, nums[:l])
        return l


nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]
nums = [0,1,1,1,1,2,2,3,3,4]

print(Solution().removeDuplicates(nums))