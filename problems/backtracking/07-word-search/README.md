## Word Search

**Difficulty**: Medium  
**Pattern**: Backtracking | DFS on Grid | Matrix Traversal  
**Link**: https://neetcode.io/problems/search-for-word/question?list=neetcode150

---

## 1. Problem Summary

Given a `m x n` grid of characters `board` and a string `word`, return `true` if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where:

- Adjacent cells are **horizontally or vertically neighboring**
- The same cell **may not be used more than once**

---

### Example 1

```text
Input:
board =
[
  ["A","B","C","E"],
  ["S","F","C","S"],
  ["A","D","E","E"]
]
word = "ABCCED"

Output: true
```

---

### Example 2

```text
Input:
board =
[
  ["A","B"],
  ["C","D"]
]
word = "ABCD"

Output: false
```

---

## 2. Key Observations

- This is a **grid traversal problem with constraints**
- We can start from **any cell** in the grid
- We must match characters **sequentially**
- Each cell can be used **only once per path**
- At each step, we explore **4 directions**:
    - up, down, left, right
- If at any point:
    - index goes out of bounds ❌
    - character mismatch ❌
    - cell already visited ❌  
      → we prune that path immediately

---

## 3. Approach 1 — Optimal (DFS + Backtracking)

### Idea

- For each cell, try to **start a DFS search**
- Match characters one by one
- Mark cells as visited during the path
- Backtrack after exploring

---

### Algorithm

1. Iterate over every cell in the grid
2. If the cell matches `word[0]`, start DFS
3. In DFS:
    - If `idx == len(word)` → return `True`
    - If out of bounds or mismatch → return `False`
    - Temporarily mark the cell as visited
    - Explore all 4 directions
    - Restore the cell (backtrack)
4. If any path returns `True`, return `True`
5. Otherwise return `False`

---

### Implementation

```python title="solution.py"
--8<-- "problems/backtracking/07-word-search/solution.py:exist"
```

---

### Complexity

Let:

- `m = number of rows`
- `n = number of columns`
- `k = length of word`

---

#### Time

```text
O(m * n * 4^k)
```

- We try starting from each cell → `m * n`
- At each step → 4 directions
- Depth of recursion → `k`

---

#### Space

```text
O(k)
```

- Recursion stack depth = length of word

---

## 4. Edge Cases

- Empty board → return `False`
- Empty word → return `True`
- Word longer than total cells → `False`
- Repeated characters in board
- Word requires revisiting same cell (not allowed)

---

## 5. Optimizations

### 🔹 Early Pruning

Check if the board contains enough characters:

```python
from collections import Counter

if Counter(word) - Counter(sum(board, [])):
    return False
```

---

### 🔹 Start from Rare Character

- If last character is rarer than first → reverse the word
- Reduces branching in DFS

---

## 6. Pattern Generalization

This problem is an example of:

- DFS on grid with **backtracking**
- **State marking (visited cells)**
- **Constraint-based path exploration**

---

### Similar problems

- Number of Islands
- Flood Fill
- Word Search II
- Path with obstacles

---

## 7. Final Takeaway

```text
Explore all paths using DFS, mark visited cells, and backtrack after exploring each path
```

> The real lesson is not the solution — it’s the pattern.