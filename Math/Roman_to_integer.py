class Solution():

    def __init__(self):
        self.romandigits={
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }  
    def romanToInt(self, s):
        # Fill this in.
        sum = 0
        prev = 0
        for i in s[::-1]:
            curr = self.romandigits[i]
            if prev > curr:
                sum -= curr
            else:
                sum += curr
            prev = curr
            #print(curr)
    
        return sum
    
    
n = 'MCMX'
print(Solution().romanToInt(n))
print(Solution().romanToInt('IX'))
print(Solution().romanToInt('XV'))
print(Solution().romanToInt('XCV'))
# 1910