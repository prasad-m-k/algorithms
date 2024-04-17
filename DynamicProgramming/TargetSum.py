#https://leetcode.com/problems/target-sum/description/

from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} #index, total
        
        def backtracking(i, total):
            if i==len(nums):
                return 1 if total==target else 0
        
            if (i, total) in dp:
                print (dp);
                return dp[(i, total)]
        
            print (dp);
            dp[(i,total)]  =  (backtracking(i+1 , total + nums[i]) + backtracking(i+1, total-nums[i]))
            return dp[(i,total)]
        
        return backtracking(0,0)
        
        

nums,target = [1,1,1,1,1], 3
nums,target = [1],  1

print(Solution().findTargetSumWays(nums, target))