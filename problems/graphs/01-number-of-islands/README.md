## Number of Islands

**Difficulty**: Medium  
**Pattern**: Matrix | DFS | BFS | Graph Traversal | Flood Fill  
**Link**: https://neetcode.io/problems/count-number-of-islands/question?list=neetcode150

---

## 1. Problem Summary

Given a 2D grid `grid` where:

- `'1'` represents land
- `'0'` represents water

Return the number of **islands**.

An island is formed by connecting adjacent lands **horizontally or vertically**.  
You may assume that the grid is surrounded by water.

---

### Example 1

```text
Input: grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]

Output: 1
```

---

### Example 2

```text
Input: grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

Output: 4
```

---

## 2. Key Observations

- The grid can be treated as a **graph**, where each cell is a node
- Connections exist in **4 directions**: up, down, left, right
- An island is essentially a **connected component of '1's**
- Once we visit a land cell, we must **mark all connected land cells as visited**
- Each time we start exploring a new unvisited `'1'`, we have found a **new island**

---

## 3. Approach 1 — DFS (Flood Fill)

---

### Idea

Traverse the grid:

- When you encounter a `'1'`, it means a new island is found
- Perform a DFS to **flood-fill** the entire island:
    - Mark all connected `'1'` cells as `'0'` (visited)
- Increment island count

---

### Algorithm

1. Initialize `count = 0`
2. Iterate over each cell `(i, j)` in the grid
3. If `grid[i][j] == '1'`:
    - Call `explore(i, j)` to traverse the island
    - Increment `count`
4. In `explore(i, j)`:
    - If out of bounds or cell is `'0'`, return
    - Mark current cell as `'0'`
    - Recursively explore all 4 directions

---

### Implementation

```python title="solution.py"
--8<-- "problems/graphs/01-number-of-islands/solution.py:num_islands_dfs"
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

Same as DFS, but instead of recursion:

```text
Use a queue to explore level by level
```

---

### Algorithm

1. Iterate over the grid
2. When `'1'` is found:
    - Start BFS from that cell
    - Push it into a queue
    - Mark it as visited
3. While queue is not empty:
    - Pop a cell
    - Explore all 4 neighbors
    - Add valid land neighbors to queue
4. Increment island count

---

### Implementation

```python title="solution.py"
from collections import deque


--8<-- "problems/graphs/01-number-of-islands/solution.py:num_islands_bfs"
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

| Aspect         | DFS             | BFS         |
|----------------|-----------------|-------------|
| Traversal      | Depth-first     | Level-order |
| Data structure | Recursion stack | Queue       |
| Risk           | Stack overflow  | Safe        |
| Performance    | Same            | Same        |

---

## 6. Edge Cases

- Empty grid → return `0`
- All water → return `0`
- All land → return `1`
- Single cell grid

---

## 7. Pattern Generalization

This problem is an example of:

- Graph traversal in a matrix
- Connected components detection
- Flood fill algorithm

---

### Similar Problems

- Max Area of Island
- Surrounded Regions
- Rotting Oranges
- Number of Provinces

---

## 8. Key Pattern Insight

```text
Each island = one connected component
```

---

## 9. Mental Model

```text
Scan grid:
→ Found '1'?
   → Explore entire island (sink it)
   → Increment count
```

---

## 10. Final Takeaway

```text
Whenever you need to count connected regions in a grid,
use DFS/BFS to explore and mark components
```

---

> The real lesson is not the solution — it’s the pattern.