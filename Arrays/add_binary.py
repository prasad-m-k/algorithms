class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = bin(int(a, 2) + int(b, 2))
        return s[2:]
    

a = "11"
b = "1"

a = "1010"
b = "1011"
print(Solution().addBinary(a,b)) 