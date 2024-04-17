#https://leetcode.com/problems/find-k-closest-elements/
from typing import List
from collections import defaultdict
import heapq
import bisect

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        print(arr)
        L = 0
        R = len(arr)-k
        while (L < R):
            print( arr[L:R], k, x)
            mid = (L+R)//2
            print(f"{arr[mid]}, {arr[mid + k]}")
            if x - arr[mid] > arr[mid + k] - x:
                L = mid + 1
            else:
                R = mid
                
                
        return arr[L: L+k]
        
        
    def findClosestElements_with_diff_array(self, arr: List[int], k: int, x: int) -> List[int]:
        diff = list(map(lambda n : abs(x-n), arr ))
        L, R = 0, len(arr)-k
        sum_min = curr_sum = sum(diff[0:k])
        min_ind=0
        while (L <= R):
            curr_sum=sum(diff[L: L+k])
            if (curr_sum < sum_min):
                sum_min = curr_sum
                min_ind = L
            L += 1
            
        
        return arr[min_ind:min_ind+k]

        
        

arr, k, x = [1,2,3,4,5], 4, -1
arr, k, x = [1], 1, 1
arr, k, x = [1,1,1,10,10,10], 1, 9
arr, k, x = [1,2,3,4,5,6,7,8,9], 4, 5

print(Solution().findClosestElements(arr,k,x))


