import math


class Solution:
    def sqrt(self, x):
        l = 0
        r = x//2 + 1
        
        while (l <= r):
            mid = l + (r - l)//2
            print(f"left={l}, right={r}, mid={mid}")
            ans = mid * mid
            if ans == x:
                return mid
            if ans < x:
                l = mid + 1
            if ans > x:
                r = mid - 1
        
        return r
            
    
    
    def sqrt1(self, num: int) -> float:

        
        left=0
        right=(num/2)+1
        
        while (left <= right):
            mid = left + (right - left)//2
            print(f"{left}, {right}, mid={mid}")
            ans = mid * mid
            if ans == num:
                print(f"mid={mid}")
                return mid
            if ans < num:
                left = mid + 1
            if ans > num:
                right = mid - 1

        print(right)
        return right



print(Solution().sqrt(25000))
print(Solution().sqrt(250))
print(Solution().sqrt(2))
print(Solution().sqrt(16))
