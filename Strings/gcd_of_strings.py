import itertools
from math import gcd

class Solution:

    def gcdOfStrings2(self, str1: str, str2: str) -> str:
        # Check if concatenated strings are equal or not, if not return ""
        if str1 + str2 != str2 + str1:
            return "XXX"
        # If strings are equal than return the substring from 0 to gcd of size(str1), size(str2)
        
        #print(gcd(len(str1),len(str2)))
        #print(gcd(len(str2)))
        return str1[:gcd(len(str1), len(str2))]

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m=len(str1)
        n=len(str2)
        
        print(f"{str1} m={m} <-> {str2} n={n}, gcd={gcd(len(str1), len(str2))}")

        if str1 + str2 != str2 + str1:
            return "-None-"
 

        if m == n:
            return str1
        
        if m > n:
            return self.gcdOfStrings(str1[n:], str2)
        return self.gcdOfStrings(str1, str2[m:])
    
str1 = "ABCDEF"
str2 = "ABC"

#print("Solution=", Solution().gcdOfStrings(str1, str2))

#exit(0)


str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
print("solution=", Solution().gcdOfStrings(str1, str2))

#exit(0)


str1 = "ABCABC"
str2 = "ABC"
#print("Solution=", Solution().gcdOfStrings(str1, str2))

#exit(0)

str1 = "ABABAB"
str2 = "ABAB"
print("Solution=", Solution().gcdOfStrings(str1, str2))
exit(0)

str1 = "LEET"
str2 = "CODE"

print("Solution=", Solution().gcdOfStrings(str1, str2))


str1 = "ABCDEFGHIJKLMNOP"
str2 = "ABCDEFGHIJKLMNOP"
print("Solution=", Solution().gcdOfStrings(str1, str2))



str1 = "ABABABA"
str2 = "ABAB"
print("Solution=", Solution().gcdOfStrings(str1, str2))
