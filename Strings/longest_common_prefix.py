#https://leetcode.com/problems/longest-common-prefix

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        mn, mx = min(strs), max(strs)
        print(mn)        
        print(mx)        

        for i in range(len(mn)):
            if mn[i] != mx[i]: return mn[:i]
             
        return mn

strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))