#Walk the matrix top to bottom right.
'''
You are given an N by M matrix of 0s and 1s. Starting from the top left corner, how many ways are there to reach the bottom right corner?
You can only move right and down. 0 represents an empty space while 1 represents a wall you cannot walk through. For example, given the following matrix:
'''

def solution(matrix, x=0, y=0):
    count = 0
    y_limit = len(matrix) - 1
    x_limit = len(matrix[0]) - 1

    # Success.
    if y == y_limit and x == x_limit:
        return 1

    # Look right.
    if x < x_limit and matrix[y][x + 1] == 0:
        count += solution(matrix, x + 1, y)

    # Look down.
    if y < y_limit and matrix[y + 1][x] == 0:
        count += solution(matrix, x, y + 1)

    return count

S=[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]

print(solution(S))
