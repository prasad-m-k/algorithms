#https://leetcode.com/problems/product-of-array-except-self/

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product=[nums[0]]
        suffix_product=[nums[-1]]
        
        for num in nums[1:]:
            prefix_product.append(prefix_product[-1]*num)
            
        for num in nums[-2::-1]:
            suffix_product.insert(0, suffix_product[0]*num)
                
        #suffix_product=list(reversed(suffix_product))   
        result=[]
        for i in range(len(nums)):
            if i == 0:
                result.append(suffix_product[i+1])
            elif i == len(nums) - 1:
                result.append(prefix_product[i-1])
            else:
                print(f"{prefix_product[i-1]} X {suffix_product[i+1]}")
                result.append(prefix_product[i-1] * suffix_product[i+1])

        print("origin=", nums)
        print("prefix=", prefix_product)
        print("suffix=", suffix_product)
        print("result=", result )
        return result 

nums=[5,4,3,2]
print(Solution().productExceptSelf(nums))