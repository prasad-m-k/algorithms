matrix = [
    [1,1,0],
    [0,1,0],
    [0,1,1]
]

matrix = [
    [1,1,0,1],
    [1,0,1,0],
    [1,1,1,0],
    [0,0,1,1]
]


n =len(matrix)

#path = [x[:] for x in [[0] * n] * n]
path = [ [0]*n for i in range(n)]
for row in path:
    print(row)

def findpath(i, j, n):
    if i == n - 1   and j == n - 1:
        path[i][j] = 1
        return 1
    if matrix[i][j] == 1:
        path[i][j] = 1
        
        if findpath(i, j + 1, n) == 1:
            return 1
        if findpath(i + 1, j, n) == 1:
            return 1
        
        path[i][j] = 0
    
    return 0


findpath(0,0,n)
print("============")
for row in path:
    print(row)
print("============")

for i, row in enumerate(path):
    for j, col in enumerate(row):
        if path[i][j] == 1:
            print(f" [{i}, {j}]", end = "->")
    

