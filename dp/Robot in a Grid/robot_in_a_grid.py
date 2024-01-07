'''
- Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
- The robot can only move in two directions, right and down, but certain cells are "offlimits" 
    such that the robot cannot step on them. 
- Design an algorithm to find a path for the robot from the top left to the bottom right.

Sample:
1 == roadblocks
[0, 1, 0, 0],
[0, 0, 0, 1],
[1, 0, 0, 0],
[0, 0, 1, 0]

[(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (2, 3), (3, 3)]
Hints:#331, #360, #388


if you are out of bounds or have a one in the direction you are going
    return
handle visited
    visited set
'''


def find_path(grid):
    
    # Handle edge cases: empty grid or no rows in the grid
    if not grid or not grid[0]:
        return []
    
    # Get the number of rows and columns in the grid
    ROW, COL = len(grid), len(grid[0])
    finalPath = []
    
    def dfs(r, c, path):
        nonlocal finalPath
        
        # Check if the current position is out of bounds or a roadblock
        if r == ROW or c == COL or grid[r][c] == 1:
            return False
        
        # Check if the robot has reached the bottom-right corner
        if (r, c) == (ROW - 1, COL - 1):
            path.append((r, c))
            finalPath = path[:]  # Update the finalPath with the valid path
            return True
        
        path.append((r, c))  # Add the current position to the path
        
        # Recursively explore the right and down directions
        res = dfs(r + 1, c, path) or dfs(r, c + 1, path)
        
        path.remove((r, c))  # Backtrack by removing the current position from the path
        return res

    # Return the finalPath if a valid path is found, or an empty list otherwise
    return finalPath if dfs(0, 0, []) else []


grid = [
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [1, 0, 0, 0],
            [0, 0, 1, 0]
        ]
val = find_path(grid)
print(val)