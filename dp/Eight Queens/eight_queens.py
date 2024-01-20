'''
EightQueens:
Write an algorithm to print all ways of arranging eight queens on an 8x8chess board 
so that none of them share the same row, column, or diagonal. In this case, "diagonal" means all
diagonals, not just the two that bisect the board.

Hints:
#308 We know that each row must have a queen. Can you try all possibilities?
#350 Each row must have a queen. Start with the last row. There are eight different columns on 
        which you can put a queen. Can you try each of these?
#371 Break this down into smaller sub problems. The queen at row 8 must be at column 
        1, 2, 3, 4, 5, 6, 7, or 8. Can you print all ways of placing eight queens where a queen 
        is at row 8 and column 3? You then need to check all the ways of placing a queen on row 7.
'''


def eight_queens(n):
    COL, DIAG, ANTI_DIAG = set(), set(), set()
    res = []
    board = [['.'] * n for _ in range(n)]
    
    def backtrack(row):
        if row == -1:
            res.append([''.join(row) for row in board])
            return
        
        for col in range(n):
            if col in COL or (row + col) in DIAG or (row - col) in ANTI_DIAG:
                continue
            
            board[row][col] = 'Q'
            COL.add(col)
            DIAG.add(row + col)
            ANTI_DIAG.add(row - col)
            
            backtrack(row - 1)
            
            board[row][col] = '.'
            COL.remove(col)
            DIAG.remove(row + col)
            ANTI_DIAG.remove(row - col)
    
    for row in range(n - 1, -1, -1):
        backtrack(row)
        
    return res

if __name__ == '__main__':
    '''
    ['..Q', 
     'Q..', 
     '...']
     
    ['Q..', 
     '..Q', 
     '...']
    
    ['Q..', 
    '...', 
    '...']
    
    ['.Q.', 
    '...', 
    '...']
    ['..Q', 
    '...', 
    '...']
    
    
    '''
    
    N = 3
    res = eight_queens(N)
    print(res)