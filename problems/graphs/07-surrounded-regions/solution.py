from util.utils import print_board


# --8<-- [start:solve]
def solve(board: list[list[str]]) -> None:
    m, n = len(board), len(board[0])

    def dfs(i, j):
        if (
                i < 0 or i >= m or
                j < 0 or j >= n or
                board[i][j] != 'O'
        ):
            return

        board[i][j] = '*'

        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    # Top and Bottom rows
    for j in range(n):
        dfs(0, j)
        dfs(m - 1, j)

    # Left and Right columns
    for i in range(m):
        dfs(i, 0)
        dfs(i, n - 1)

    for i in range(m):
        for j in range(n):
            if board[i][j] == '*':
                board[i][j] = 'O'
            elif board[i][j] == 'O':
                board[i][j] = 'X'


# --8<-- [end:solve]

b = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "X", "O"]
]
solve(b)
print_board(b)
