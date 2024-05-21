from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []

        top_row = 0
        bottom_row = len(matrix) - 1
        left_col = 0
        right_col = len(matrix[0]) - 1

        while top_row <= bottom_row and left_col <= right_col:

            for i in range(left_col, right_col + 1):
                output.append(matrix[top_row][i])
            top_row += 1

            for i in range(top_row, bottom_row + 1):
                output.append(matrix[i][right_col])
            right_col -= 1

            if top_row > bottom_row: break

            for i in range(right_col, left_col - 1, -1):
                output.append(matrix[bottom_row][i])
            bottom_row -= 1 

            if left_col > right_col: break

            for i in range(bottom_row, top_row - 1, -1):
                output.append(matrix[i][left_col])
            left_col += 1  

        return output                

    
    def spiralOrder3(m: List[List[int]]) -> List[int]:
        return m and [*m[0]]+self.spiralOrder3([*zip(*m[1:])][::-1])


# Example usage:
matrix = [
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [7, 8, 9, 0]
]
print("Spiral order:", Solution().spiral_order(matrix))
print("Spiral order:", Solution().spiralOrder3(matrix))
