## Print All Permutations of a String/Array
def permute(s):
    result = []
    def backtrack(start):
        if start == len(s):
            result.append(''.join(s))
            return
        for i in range(start, len(s)):
            s[start], s[i] = s[i], s[start]  # Swap
            backtrack(start + 1)
            s[start], s[i] = s[i], s[start]  # Backtrack (swap back)

    backtrack(0)
    return result
print(permute(list("abc")))

## N Queen Problem | Return all Distinct Solutions to the N-Queens Puzzle
def solveNQueens(n):
    def is_safe(board, row, col):
        # Check this column on upper side
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        # Check upper diagonal on right side
        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i][j] == 'Q':
                return False
        return True

    def solve(board, row):
        if row >= n:
            result.append([''.join(r) for r in board])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                solve(board, row + 1)
                board[row][col] = '.'  # Backtrack

    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    solve(board, 0)
    return result
print(solveNQueens(4))
print(solveNQueens(1))