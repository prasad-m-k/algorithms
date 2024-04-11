#https://leetcode.com/problems/valid-palindrome-ii/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def ispal(s):
            i, rev = 0, len(s) - 1
            print(f"s={s}, i={i}, rev={rev}")
            while i < rev:
                if s[i] != s[rev]:
                    return False
                i += 1
                rev -= 1
                    
            #print(f"s={s} is a Palindrome")
            return True

        i, rev = 0, len(s) - 1
        while i < rev:
            if s[i] != s[rev]:
                return ispal(s[i: rev]) or ispal(s[i+1: rev+1])
            i += 1
            rev -= 1
        return True

        '''
        print(f"s={s}")
        L=0
        R=len(s)-1
        #if R < 0:
        #    return False
        while(L<=R):
            if s[L] == s[R]:
                L += 1
                R -= 1
            else:
                if L+1 >= R-1:
                    return False
                ret = self.validPalindrome(s[L+1:R-1])
                if ret:
                    L += 1
                    R -= 1
                    continue
                return False
        
        return True
        '''
    


s3 = "abca"

s3 = "eedede"
s3 = "abc"
s3 = "aba"
s3 = "abca"
s3 = "abc"
s3 = "eeccccbebaeeabebccceea"
s3 = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"

#print(f"{s1} => {Solution().validPalindrome(s1)}")
#print(f"{s2} => {Solution().validPalindrome(s2)}")
print(f"{s3} => {Solution().validPalindrome(s3)}")
#print(f"{s[L+1]} != {s[R]}, L+1={L+1}, R={R}")
#print(f"{s[L]} != {s[R-1]}, L={L}, R-1={R-1}")
