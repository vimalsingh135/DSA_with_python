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

## Sudoku Solver
def sudoku_solver(board):
    def is_valid(r,c,val):
        for i in range(9):
            if board[r][i] == val or board[i][c] == val:
                return False

            box_r=3*(r//3)+i//3
            box_c=3*(c//3)+i%3
            if board[box_r][box_c] == val:
                return False
        return True

    def solve():
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    for val in range(1,10):
                        if is_valid(r,c,val):
                            board[r][c] = val
                            if solve():
                                return True
                            board[r][c] = 0
                    return False
        return True

    solve()
    return board
print(sudoku_solver([[5,3,0,0,7,0,0,0,0],
                      [6,0,0,1,9,5,0,0,0],
                      [0,9,8,0,0,0,0,6,0],
                      [8,0,0,0,6,0,0,0,3],
                      [4,0,0,8,0,3,0,0,1],
                      [7,0,0,0,2,0,0,0,6],
                      [0,6,0,0,0,0,2,0,0],
                      [0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0]]))

## M - Coloring Problem
## Problem Statement: Given an undirected graph and a number m, determine if the graph can be colored with at most m colors such that no two adjacent vertices of the graph are colored with the same color.
def graph_coloring(graph, m):
    def is_safe(node, color):
        for neighbor in graph[node]:
            if color_assignment[neighbor] == color:
                return False
        return True

    def solve(node):
        if node == len(graph):
            return True
        for color in range(1, m + 1):
            if is_safe(node, color):
                color_assignment[node] = color
                if solve(node + 1):
                    return True
                color_assignment[node] = 0  # Backtrack
        return False

    color_assignment = [0] * len(graph)
    if solve(0):
        return color_assignment
    else:
        return None

## Rat in a Maze
## Problem Statement: Given a grid of dimensions n x n. A rat is placed at coordinates (0, 0) and wants to reach at coordinates (n-1, n-1). Find all possible paths that rat can take to travel from (0, 0) to (n-1, n-1). The directions in which rat can move are 'U' (up) , 'D' (down) , 'L' (left) , 'R' (right).
## The value 0 in grid denotes that the cell is blocked and rat cannot use that cell for travelling, whereas value 1 represents that rat can travel through the cell. If the cell (0, 0) has 0 value, then mouse cannot move to any other cell.

def ratInMaze(n, grid):
    result = []
    visited = [[False]*n for _ in range(n)]
    
    # direction order matters for alphabetical output: D, L, R, U
    dr = [1, 0, 0, -1]
    dc = [0, -1, 1, 0]
    dirName = ['D', 'L', 'R', 'U']
    
    def isSafe(r, c):
        return 0 <= r < n and 0 <= c < n and grid[r][c] == 1 and not visited[r][c]
    
    def solve(r, c, path):
        if r == n-1 and c == n-1:
            result.append(path)      # reached destination, save this path
            return
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if isSafe(nr, nc):
                visited[nr][nc] = True          # mark visited (commit to this move)
                solve(nr, nc, path + dirName[i]) # recurse deeper
                visited[nr][nc] = False         # backtrack (undo the move)
    
    if grid[0][0] == 1:
        visited[0][0] = True
        solve(0, 0, "")
    
    return result
print (ratInMaze(4, [[1, 0, 0, 0],
                    [1, 1, 0, 1],
                    [0, 1, 0, 0],
                    [1, 1, 1, 1]]))


## word Break Problem

def wordBreak(s, wordDict):
    wordSet = set(wordDict)   # O(1) lookup instead of scanning the list
    n = len(s)
    
    # dp[i] = True means: the substring s[i:] CAN be fully segmented
    dp = [False] * (n + 1)
    dp[n] = True   # empty string (we reached the very end) is always "breakable"
    
    # work backwards from the end of the string to the start
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n + 1):
            # s[i:j] is one candidate word, s[j:] is "the rest"
            if s[i:j] in wordSet and dp[j]:
                dp[i] = True
                break   # found one way to break from i, no need to check more
    
    return dp[0]