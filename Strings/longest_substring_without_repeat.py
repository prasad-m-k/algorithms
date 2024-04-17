class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        print(s)
        n = len(s)
        ans = 0
        charmap={}

        i = 0
        for j in range(n):
            if s[j] in charmap:
                i = max(charmap[s[j]], i)
                print(i, s[j])
            
            ans = max(ans, j - i + 1)
            charmap[s[j]] = j + 1


        print(charmap)        
        return ans


s = "bbbbb"
s = "pwwkew"
s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))