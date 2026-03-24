# --8<-- [start:exist]
def exist(board: list[list[str]], word: str) -> bool:
    def in_bounds(i, j):
        return 0 <= i < rows and 0 <= j < cols

    def search(i: int, j: int, idx: int):
        if idx == len(word):
            return True
        if not in_bounds(i, j) or board[i][j] != word[idx]:
            return False

        t = board[i][j]
        board[i][j] = '*'

        found = search(i + 1, j, idx + 1) or \
                search(i - 1, j, idx + 1) or \
                search(i, j + 1, idx + 1) or \
                search(i, j - 1, idx + 1)

        board[i][j] = t
        return found

    rows, cols = len(board), len(board[0])
    for x in range(0, rows):
        for y in range(0, cols):
            if board[x][y] == word[0] and search(x, y, 0):
                return True

    return False


# --8<-- [end:exist]

b = [
    ["A", "B", "C", "D"],
    ["S", "A", "A", "T"],
    ["A", "C", "A", "E"]
]
w = "CAT"

print(exist(b, w))
