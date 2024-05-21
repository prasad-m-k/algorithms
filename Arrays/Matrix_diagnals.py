
grid = [
    ["1", "1", "0", "0"],
    ["1", "1", "0", "0"],
    ["0", "0", "1", "0"],
    ["0", "0", "0", "1"]
]

first = []
second = []
def printdiag(grid):
    for i, row in enumerate(grid):
        for j, col in enumerate(grid[i]):
            if i==j:
                first.append(grid[i][j])
            elif (i + j) == len(grid) - 1:
                second.append(grid[i][j])
    
    return( first, second )

print(printdiag(grid))