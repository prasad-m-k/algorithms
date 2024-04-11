#https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome1(self, s: str) -> bool:
        x=''.join([c.lower() for c in s if c.isalnum()])
        return x==x[::-1]

    def isPalindrome(self, s: str) -> bool:
        L=0
        R=len(s)-1
        while (L < R):
            if not s[L].isalnum():
                L += 1
                continue
            if not s[R].isalnum():
                R -= 1
                continue
            if s[L].lower() != s[R].lower():
                return False
            L += 1
            R -= 1
        return True

s="0P"
s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))
        