#https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/description/

import string

class Solution:
    def minTimeToType(self, word: str) -> int:
        ret = len(word)
        dist = 0
        word = "a" + word
        ind = 1
        while (ind < ret+1):
            fwd = (ord(word[ind]) - ord(word[ind-1])) % 26
            rev = (ord(word[ind-1]) - ord(word[ind])) % 26
            #print(f"fwd={fwd}, rev={rev}")
            dist += min( fwd, rev)
            ind += 1
        
        ret += dist
        print(f"ans={ret}")
        return ret
    
    
    
    

Solution().minTimeToType("abc")
Solution().minTimeToType("bza")
Solution().minTimeToType("zjpc")