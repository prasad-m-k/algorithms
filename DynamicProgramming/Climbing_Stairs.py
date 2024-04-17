#https://leetcode.com/problems/climbing-stairs/description/



class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1,1
        
        for i in range(n-1):
            #temp = one
            #one = one + two
            #two = temp
            one, two = two+one, one
        
        return one
    

print(Solution().climbStairs(5))