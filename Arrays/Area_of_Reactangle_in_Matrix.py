#https://www.techiedelight.com/find-largest-rectangle-of-1s-binary-matrix/
##
#Find the area of the largest rectangle of 1’s in a binary matrix
##

# Utility function to replace all non-zero values in a matrix by 1
def resetMatrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] != 0:
                mat[i][j] = 1
 
 
# Function to calculate the area of the largest rectangle of 1's where swapping of
# columns is allowed
def findMaxRectArea(mat):
 
    # base case
    if not mat or not len(mat):
        return 0
 
    # `M × N` matrix
    M = len(mat)
    N = len(mat[0])
 
    # update the matrix to store the counts of consecutive 1's present in each column
    for j in range(N):
        # process each column from bottom to top
        for i in reversed(range(0, M - 1)):
            if mat[i][j] == 1:
                mat[i][j] = mat[i + 1][j] + 1
 
    # keep track of the largest rectangle of 1's found so far
    maxArea = 0
 
    # traverse each row in the modified matrix to find the maximum area
    for i in range(M):
 
        # create a count array for each row `i`
        count = [0] * (M + 1)
 
        # process row `i`
        for j in range(N):
 
            if mat[i][j] > 0:
 
                # increment value in the count array using the current element
                # as an index
                count[mat[i][j]] += 1
 
                # the area can be calculated by multiplying the current
                # element `mat[i][j]` with the corresponding value in the
                # count array `count[mat[i][j]]`
 
                maxArea = max(maxArea, mat[i][j] * count[mat[i][j]])
 
    # reset matrix before returning
    resetMatrix(mat)
 
    return maxArea
 
 
if __name__ == '__main__':
 
    mat = [
        [0, 1, 0, 1, 1],
        [1, 1, 0, 0, 1],
        [1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1]
    ]
 
    print("The area of the largest rectangle of 1's is", findMaxRectArea(mat))
 