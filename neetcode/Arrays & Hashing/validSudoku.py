
def isValidSudoku(self, board: List[List[str]]) -> bool:
    sCol = defaultdict(set)
    sRow = defaultdict(set)
    sRowCol = defaultdict(set) # key (r // 3, c // 3) -> val
    
    ROW = 9
    COL = 9
    BOX = 3
    for i in range(ROW):
        for j in range(COL):
            
            # ignore empty cells
            if board[i][j] == '.':
                continue
                
            # check if in set
            if (board[i][j] in sRow[i] or                      # in same column
                board[i][j] in sCol[j] or                      # in same row
                board[i][j] in sRowCol[ (i // 3, j // 3) ]  # in same 3x3 box
                ):
                return False
            
            sCol[j].add(board[i][j])
            sRow[i].add(board[i][j])
            sRowCol[(i // 3, j // 3)].add(board[i][j])
            
            print(sCol)
                
    return True
