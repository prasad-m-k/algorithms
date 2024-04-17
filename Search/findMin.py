#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        #if len(nums) == 1:
        #    return nums[0]
        L, R = 0, len(nums)-1
        result = nums[0]        

        while(L <= R):
            if nums[L] < nums[R]:
                result = min(result, nums[L])
                print(f"result={result}, L={L}, R={R}, {nums[L]}, {nums[R]}")
                break
            
            M = (L+R)//2
            result = min(result, nums[M])
            print(f"result={result}, L={L}, R={R}, {nums[L]}, {nums[R]}")

            if nums[M] >= nums[L]:
                L = M+1
            else:
                R = M -1
                

        print(result)
        return result

        
        

nums = [3,4,5,1,2]
nums = [11,13,15,17,4,5,6,7,0,1,2]
Solution().findMin(nums)


'''
L = 0
R = len(nums) -1

if nums[R] > nums[L]:
    return nums[L]

while( L <= R):
    mid = L + (R-L)//2
    if nums[mid] > nums[mid +1]:
        return nums[mid+1]
    if nums[mid - 1] > nums[mid]:
        return nums[mid]
    if nums[mid] > nums[0]:
        L = mid + 1
    else:
        R = mid - 1
'''        
