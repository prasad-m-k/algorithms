def num_islands(grid):
    if not grid:
        return 0

    def dfs(i, j):
        #print(f"dfs of [{i},{j}] ")
        # Check if the current cell is out of bounds or water
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return
        
        # Mark the current cell as visited by setting it to '0' (water)
        print(f"[{i},{j}] = '0'")
        grid[i][j] = '0'
        for row in grid:
            print(row)
        
        # Explore the neighboring cells in four possible directions (up, down, left, right)
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    island_count = 0
    
    # Iterate over every cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1':  # Found an unvisited land cell
                dfs(i, j)
                island_count += 1  # Increment island count for each new island found

    return island_count

# Example usage
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

for row in grid:
    print(row)
print("Number of islands:", num_islands(grid))
for row in grid:
    print(row)
