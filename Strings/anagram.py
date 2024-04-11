#https://leetcode.com/problems/valid-anagram/
from collections import Counter

class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:
        #return Counter(s) == Counter(t)
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        print(s, t)
        return s==t
    
    def isAnagram2(self, s: str, t: str) -> bool:
        s_map={}
        t_map={}
        for c in s:
            if c in s_map:
                s_map[c] += 1
            else:
                s_map[c] = 1
        for c in t:
            if c in t_map:
                t_map[c] += 1
            else:
                t_map[c] = 1
    
        print(s_map)
        print(t_map)
        x=Counter(s)
        print(x)
        return s_map==t_map
    
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

s, t = "rat", "car"
s, t = "anagram", "nagaram"

print(f"{s} <=> {t} {Solution().isAnagram(s,t)}")