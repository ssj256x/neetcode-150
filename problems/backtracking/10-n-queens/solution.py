# --8<-- [start:n_queens]
def solve_n_queens(n: int) -> list[list[str]]:
    def is_valid(row, col):
        for r in range(row):
            if board[r][col] == 'Q':
                return False

        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c -= 1

        r, c = row - 1, col + 1
        while r >= 0 and c < n:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c += 1

        return True

    def place(row):
        if row == n:
            ans.append(["".join(r) for r in board])

        for col in range(n):
            if is_valid(row, col):
                board[row][col] = 'Q'
                place(row + 1)
                board[row][col] = '.'

    ans = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    place(0)
    return ans


# --8<-- [end:n_queens]

def print_board(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            print(f'{b[i][j]} ', end="")
        print()
    print('-' * (len(b) * 2 - 1))


queens = 6
for b in solve_n_queens(queens):
    print_board(b)
