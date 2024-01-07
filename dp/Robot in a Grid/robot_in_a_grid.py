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
[(0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3)]

Hints:#331, #360, #388


if you are out of bounds or have a one in the direction you are going
    return
handle visited
    visited set
'''


def find_path(grid):
    
    # handle 0 edge cases
    if not grid:
        return None
    if not grid[0]:
        return ([0,0])
    
    ROW, COL = len(grid), len(grid[0])
    visited = set()
    finalPath = -99
    
    
    def dfs(r, c, path):
        # handle boundary and road block case
        if r == ROW or c == COL or (r, c) in visited or grid[r][c] == 1:
            return
        
        if (r, c) == (ROW - 1, COL - 1):
            path.append((r, c))    
            return path
        
        visited.add((r, c))
        path.append((r, c))
        
        # dfs into other indices
        x = dfs(r + 1, c, path) # down
        y = dfs(r, c + 1, path) # right
        
        visited.remove((r, c))
        path.remove((r, c))
        
        if x: print(x)
        if y: print(y)
        
        
    return dfs(0, 0, [])

grid = [
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [1, 0, 0, 0],
            [0, 0, 1, 0]
        ]
val = find_path(grid)
print(val)