def is_valid_sudoku_sub_optimal(board: list[list[str]]) -> bool:
    for i in range(0, 9):
        seen = set()
        for j in range(0, 9):
            cur = board[i][j]
            if cur == '.':
                continue
            if cur in seen:
                return False
            seen.add(cur)

    for i in range(0, 9):
        seen = set()
        for j in range(0, 9):
            cur = board[j][i]
            if cur == '.':
                continue
            if cur in seen:
                return False
            seen.add(cur)

    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            seen = set()

            for i in range(0, 3):
                for j in range(0, 3):
                    cur = board[row + i][col + j]
                    if cur == '.':
                        continue
                    if cur in seen:
                        return False
                    seen.add(cur)

    return True


def is_valid_sudoku_optimal(board: list[list[str]]):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for r in range(0, 9):
        for c in range(0, 9):
            cur = board[r][c]

            if cur == '.':
                continue

            box = (r // 3) * 3 + (c // 3)

            if cur in rows[r] or cur in cols[c] or cur in boxes[box]:
                return False

            rows[r].add(cur)
            cols[c].add(cur)
            boxes[box].add(cur)

    return True


def is_valid_sudoku_most_optimal(board: list[list[str]]):
    seen = set()

    for r in range(0, 9):
        for c in range(0, 9):
            cur = board[r][c]

            if cur == '.':
                continue

            row_key = (cur, r)
            col_key = (c, cur)
            box_key = (r // 3, c // 3, cur)

            if row_key in seen or col_key in seen or box_key in seen:
                return False

            seen.add(row_key)
            seen.add(col_key)
            seen.add(box_key)

    return True


b = [["1", "2", ".", ".", "3", ".", ".", ".", "."],
     ["4", ".", ".", "5", ".", ".", ".", ".", "."],
     [".", "9", "8", ".", ".", ".", ".", ".", "3"],
     ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
     [".", ".", ".", "8", ".", "3", ".", ".", "5"],
     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", ".", ".", ".", ".", ".", "2", ".", "."],
     [".", ".", ".", "4", "1", "9", ".", ".", "8"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(is_valid_sudoku_most_optimal(b))
