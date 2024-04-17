#https://leetcode.com/problems/search-a-2d-matrix/description/

from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        print(matrix)
        ROWS=len(matrix)
        COLS=len(matrix[0])
        
        print("size=", ROWS, " X ", COLS)
        L = 0
        R = len(matrix[0]) -1
        T = 0
        B = len(matrix) - 1
        print(f"top-left={matrix[T][L]}, bottom-left={matrix[B][L]}")
        print(f"top-right={matrix[T][R]}, bottom-right={matrix[B][R]}")
        
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m*n - 1
        print(f"left={left}, right={right}")
        while left <= right:
            mid = (left + right)//2
            mid_row, mid_col = divmod(mid, n)
            
            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                left = mid + 1
            elif matrix[mid_row][mid_col] > target:
                right = mid - 1
        
        return False



matrix, target = [[1,3,5,7],[10,11,16,20],[23,30,34,60]],  3

print(Solution().searchMatrix(matrix, target))