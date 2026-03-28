## N Queens

**Difficulty**: Hard  
**Pattern**: Backtracking | Array  
**Link**: https://neetcode.io/problems/n-queens/question?list=neetcode150

---

## 1. Problem Summary

The **N-Queens** problem asks you to place `n` queens on an `n x n` chessboard such that:

```text
No two queens attack each other
```

A queen can attack:

- Horizontally (row)
- Vertically (column)
- Diagonally

---

### Goal

Return all distinct solutions where each solution is represented as a board configuration.

Each board is represented as a list of strings:

- `'Q'` → Queen
- `'.'` → Empty cell

---

### Example

```text
Input: n = 4

Output:
[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
```

---

## 2. Key Observations

- Only **one queen per row** is allowed
- This allows us to reduce a **2D problem → 1D recursion**
- At each row, we only decide **which column to place the queen**
- We must ensure:
    - No two queens share the same column
    - No two queens share the same diagonal

---

## 3. Approach 1 — Backtracking with Board Scan

---

### Idea

- Place queens row by row
- For each position, check if placing a queen is valid by scanning:
    - Column
    - Left diagonal
    - Right diagonal
- If valid:
    - Place queen
    - Recurse to next row
    - Backtrack

---

### Algorithm

1. Start from `row = 0`
2. For each column in the row:
    - Check if position is valid
3. If valid:
    - Place `'Q'`
    - Recurse for next row
    - Remove `'Q'` (backtrack)
4. If `row == n`:
    - Add current board to result

---

### Code

```python
def solve_n_queens(n: int) -> list[list[str]]:
    def is_valid(row: int, col: int) -> bool:
        # Column check
        for r in range(row):
            if board[r][col] == 'Q':
                return False

        # Left diagonal ↖
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c -= 1

        # Right diagonal ↗
        r, c = row - 1, col + 1
        while r >= 0 and c < n:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c += 1

        return True

    def backtrack(row: int):
        if row == n:
            ans.append(["".join(r) for r in board])
            return

        for col in range(n):
            if is_valid(row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

    board = [['.' for _ in range(n)] for _ in range(n)]
    ans = []
    backtrack(0)
    return ans
```

---

### Complexity

#### Time

```
O(N!)
```

- Each row has at most `n` choices
- But constraints prune many branches early

---

#### Space

```
O(N)
```

- Recursion depth = `n`
- Board storage excluded from recursion stack

---

### Drawback

```text
Checking validity takes O(n) time per placement
```

---

## 4. Approach 2 — Optimized Backtracking (O(1) Checks)

---

### Core Insight

Instead of scanning the board repeatedly:

```text
Track occupied columns and diagonals using sets
```

---

### Data Structures

```text
cols       → occupied columns
diag       → (row - col) → main diagonals
anti_diag  → (row + col) → anti-diagonals
```

---

### Why It Works

- Same column → same `col`
- Same diagonal → same `row - col`
- Same anti-diagonal → same `row + col`

---

### Algorithm

1. Start from `row = 0`
2. For each column:
    - Skip if column or diagonals are already occupied
3. If valid:
    - Place queen
    - Mark sets
    - Recurse
    - Backtrack and unmark

---

### Code

```python
def solve_n_queens(n: int) -> list[list[str]]:
    def backtrack(row: int):
        if row == n:
            ans.append(["".join(r) for r in board])
            return

        for col in range(n):
            if (
                    col in cols or
                    (row - col) in diag or
                    (row + col) in anti_diag
            ):
                continue

            board[row][col] = 'Q'
            cols.add(col)
            diag.add(row - col)
            anti_diag.add(row + col)

            backtrack(row + 1)

            board[row][col] = '.'
            cols.remove(col)
            diag.remove(row - col)
            anti_diag.remove(row + col)

    board = [['.' for _ in range(n)] for _ in range(n)]
    cols = set()
    diag = set()
    anti_diag = set()
    ans = []

    backtrack(0)
    return ans
```

---

### Complexity

#### Time

```
O(N!)
```

- Same search space, but faster pruning

---

#### Space

```
O(N)
```

- Sets + recursion stack

---

## 5. Edge Cases

- `n = 1` → single solution
- `n = 2 or 3` → no valid solutions
- Larger `n` → exponential growth in solutions

---

## 6. Pattern Generalization

This problem is an example of:

- Backtracking (DFS)
- Constraint Satisfaction Problem
- Pruning using state tracking

---

### Similar Problems

- Sudoku Solver
- Word Search
- Generate Parentheses
- Combination Sum

---

## 7. Key Pattern Insight

```text
Reduce a 2D placement problem into a 1D decision per step
```

---

## 8. Mental Model

```text
Row by row:
→ Try placing a queen in each column
→ Skip invalid placements
→ Recurse
→ Backtrack
```

---

## 9. Final Takeaway

```text
Backtracking becomes powerful when combined with pruning,
and constraints can often reduce dimensionality
```

---

> The real lesson is not the solution — it’s the pattern.