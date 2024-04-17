def spiral_order(matrix):
    if not matrix:
        return []

    result = []
    top_row, bottom_row = 0, len(matrix) - 1
    left_col, right_col = 0, len(matrix[0]) - 1

    while left_col <= right_col and top_row <= bottom_row:
        # Traverse from left_col to right_col across the top_row
        for i in range(left_col, right_col + 1):
            result.append(matrix[top_row][i])
        top_row += 1

        # Traverse downwards on the right_col side
        for i in range(top_row, bottom_row + 1):
            result.append(matrix[i][right_col])
        right_col -= 1

            # Traverse from right_col to left_col across the bottom_row
        for i in range(right_col, left_col - 1, -1):
            result.append(matrix[bottom_row][i])

        if top_row <= bottom_row:
            bottom_row -= 1

            # Traverse upwards on the left_col side
        for i in range(bottom_row, top_row - 1, -1):
            result.append(matrix[i][left_col])

        if left_col <= right_col:
            left_col += 1

    return result

# Example usage:
matrix = [
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [7, 8, 9, 0]
]
print("Spiral order:", spiral_order(matrix))