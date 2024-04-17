#https://leetcode.com/problems/palindromic-substrings/
#Facebook 12
'''
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        ret = 0

        if N == 0:
            return 0
        
        dp = [[0]*N]*N
        
        for i in range(N):
            dp[i][i] = True
            ret += 1
        
        for i in range(N-1):
            dp[i][i+1] = True if s[i] == s[i+1] else False
            ret += dp[i][i+1]

        
        for L in range(3, N):
            i = 1
            j = i + L -1
            while j < N:
                dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                ret += dp[i][j]


        return ret



