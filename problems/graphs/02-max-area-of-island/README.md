## Max Area of Island

**Difficulty**: Medium  
**Pattern**: Matrix | DFS | BFS | Graph Traversal | Flood Fill  
**Link**: https://neetcode.io/problems/max-area-of-island/question?list=neetcode150

---

## 1. Problem Summary

Given a 2D grid `grid` of `0`s and `1`s:

- `1` → land
- `0` → water

Return the **maximum area of an island**.

An island is formed by connecting adjacent lands **horizontally or vertically**.

---

### Example

```text
Input:
[
 [0,1,1,0,1],
 [1,0,1,0,1],
 [0,1,1,0,1],
 [0,1,0,0,1]
]

Output: 5
```

---

## 2. Key Observations

- This is an extension of **Number of Islands**
- Instead of counting islands, we compute **size of each island**
- Each island is a **connected component of 1s**
- We can use **DFS or BFS** to explore an island
- While exploring, we **accumulate size**
- Take the **maximum over all islands**

---

## 3. Approach 1 — DFS (Recursive Flood Fill)

---

### Idea

- When we encounter a `1`, start a DFS
- Recursively explore all connected land cells
- Count the total number of cells visited
- Return the size of the island
- Track the maximum

---

### Algorithm

1. Iterate over all cells
2. If `grid[i][j] == 1`:
    - Call `explore(i, j)`
    - Update `max_size`
3. In `explore(i, j)`:
    - If out of bounds or `0`, return `0`
    - Mark current cell as visited (`0`)
    - Return:
      ```
      1 + explore(all 4 directions)
      ```

---

### Implementation

```python
--8<-- "problems/graphs/02-max-area-of-island/solution.py:max_area_of_island_dfs"
```

---

### Complexity

Let `m = rows`, `n = cols`

#### Time

```
O(m * n)
```

- Each cell is visited once

---

#### Space

```
O(m * n)
```

- Worst case recursion stack (all land)

---

## 4. Approach 2 — BFS (Queue-Based Flood Fill)

---

### Idea

- Same as DFS, but use a queue instead of recursion
- Explore the island level by level
- Count the number of visited cells

---

### Algorithm

1. Iterate over grid
2. When `1` is found:
    - Start BFS
    - Initialize `size = 1`
3. While queue is not empty:
    - Pop a cell
    - Explore all 4 neighbors
    - Add valid land cells to queue
    - Increment `size`
4. Update `max_size`

---

### Implementation

```python
from collections import deque


--8<-- "problems/graphs/02-max-area-of-island/solution.py:max_area_of_island_bfs"
```

---

### Complexity

#### Time

```
O(m * n)
```

---

#### Space

```
O(m * n)
```

- Queue in worst case (all land)

---

## 5. DFS vs BFS

| Aspect         | DFS            | BFS         |
|----------------|----------------|-------------|
| Traversal      | Depth-first    | Level-order |
| Data structure | Recursion      | Queue       |
| Risk           | Stack overflow | Safe        |
| Performance    | Same           | Same        |

---

## 6. Common Pitfalls

- Mixing types (`1` vs `'1'`, `0` vs `'0'`)
- Not marking visited → infinite loops
- Missing boundary checks
- Mutating input unintentionally (if not allowed)

---

## 7. Edge Cases

- Empty grid → `0`
- All water → `0`
- All land → `m * n`
- Single cell grid

---

## 8. Pattern Generalization

This problem is an example of:

- Connected components in a grid
- Flood fill algorithm
- Graph traversal (DFS/BFS)

---

### Similar Problems

- Number of Islands
- Surrounded Regions
- Rotting Oranges
- Walls and Gates

---

## 9. Key Pattern Insight

```text
Each island = one connected component
→ explore it fully → compute its size
```

---

## 10. Mental Model

```text
Scan grid:
→ Found land?
   → Explore entire island
   → Count size
   → Track maximum
```

---

## 11. Final Takeaway

```text
Whenever you need to compute properties of connected regions in a grid
(size, count, shape), use DFS/BFS flood fill
```

---

> The real lesson is not the solution — it’s the pattern.