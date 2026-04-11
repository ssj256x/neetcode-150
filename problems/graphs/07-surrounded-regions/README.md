## Problem Name

**Difficulty**: Medium  
**Pattern**: Graph | DFS/BFS | Flood Fill (Boundary Traversal)  
**Link
**: <a href="https://neetcode.io/problems/surrounded-regions/question?list=neetcode150" target="_blank">https://neetcode.io/problems/surrounded-regions/question?list=neetcode150</a>

---

## 1. Problem Summary

You are given a 2D board containing `'X'` and `'O'`.

- `'X'` → blocked cell
- `'O'` → open cell

A region of `'O'` is **captured** if it is completely surrounded by `'X'`.

👉 Replace all captured regions with `'X'`.

Return the modified board **in-place**.

---

## 2. Key Observations

- A region is captured **only if it is NOT connected to the boundary**
- Any `'O'` connected to the border can NEVER be captured
- Instead of finding regions to capture directly, it's easier to:
    - Find regions that are **safe (not capturable)**

Hence we apply:

- Boundary traversal
- Flood fill (DFS/BFS)
- Mark safe regions first, then flip the rest

---

## 3. Approach 1 — Optimal

### Idea

Instead of checking every region individually:

1. Traverse the **boundary cells**
2. For every `'O'` on the boundary:
    - Run DFS/BFS and mark all connected `'O'` as **safe**
3. After marking:
    - Convert all remaining `'O'` → `'X'` (captured)
    - Convert safe markers back to `'O'`

---

### Algorithm

- Iterate over boundary cells:
    - First row, last row
    - First column, last column
- If a boundary cell is `'O'`:
    - Run DFS/BFS:
        - Mark all connected `'O'` as `'T'` (temporary safe marker)
- Traverse entire board:
    - If `'O'` → convert to `'X'` (captured)
    - If `'T'` → convert back to `'O'` (safe)

---

### Implementation

```python title="solution.py"
--8<-- "problems/graphs/07-surrounded-regions/solution.py:solve"
```

---

### Complexity

- **Time**: `O(n * m)` — each cell visited at most once
- **Space**: `O(n * m)` worst case recursion/queue

---

## 4. Edge Cases

- Empty board → no changes
- All `'X'` → no changes
- All `'O'` → none captured (all connected to boundary)
- Single row/column → no enclosed regions possible
- Narrow corridors connecting to boundary → should remain `'O'`

---

## 5. Pattern Generalization

This problem is an example of:

- Flood fill from boundary
- Reverse thinking (mark what NOT to change)
- Connected components in a grid

Similar problems:

- Number of Islands
- Pacific Atlantic Water Flow
- Walls and Gates
- Flood Fill

---

## 6. Final Takeaway

> When asked to capture or modify enclosed regions, think in reverse:  
> **Start from the boundary and mark what is safe.**

Everything not connected to the boundary is implicitly enclosed and can be modified.