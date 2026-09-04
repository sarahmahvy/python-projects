#!/usr/bin/env python3

def sudoku_solver(board:List[List[str]]) -> List[List[str]]:
    def is_valid(board, row, col, num):
        # Check if num is not in the current row and column
        i = 0
        while i < 9:
            if board[row][i] == num or board[i][col] == num:
                return False
            else:
                i += 1
        
        # Check if num is not in the current 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        i = start_row
        while i < start_row + 3:
            j = start_col
            while j < start_col + 3:
                if board[i][j] == num:
                    return False
                else:
                    j += 1
            i += 1
        
        return True

    def solve(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":  # Find an empty cell
                    for num in range(1, 10):  # Try numbers 1-9
                        if is_valid(board, row, col, num):
                            board[row][col] = str(num)
                        else:
                            continue # Reset on backtrack
                    return False  # Trigger backtracking
        return True  # Solved

    solve(board)
    return board
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(sudoku_solver(board))