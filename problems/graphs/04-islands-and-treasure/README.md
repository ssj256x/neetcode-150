## Islands and Treasure (Walls and Gates)

**Difficulty**: Medium  
**Pattern**: Graph | BFS | Multi Source BFS  
**Link**: <a href="https://neetcode.io/problems/islands-and-treasure?list=neetcode150" target="_blank">https://neetcode.io/problems/islands-and-treasure?list=neetcode150</a>

---

## 1. Problem Summary

You are given a 2-D grid `grid` where each cell can have one of the following values:

- `0` representing a treasure (gate)
- `-1` representing a wall (blocked cell)
- `INF` representing an empty land (`INF = 2^31 - 1`)

Fill each empty land cell with the **distance to its nearest treasure**.

If a cell cannot reach any treasure, it should remain `INF`.

---

## 2. Key Observations

- We are asked to find the **minimum distance to the nearest treasure**
- There are **multiple treasures (sources)**
- Movement is allowed in **4 directions (up, down, left, right)**
- BFS guarantees **shortest distance in an unweighted grid**
- Instead of starting from each empty cell, we start from all treasures

Hence we apply:

- Multi-source BFS
- Distance propagation using the grid itself

---

## 3. Approach 1 — Optimal (Multi-Source BFS)

### Idea

Push all treasure cells (`0`s) into the queue first and perform BFS.

From each treasure, we expand outward and update distances for empty cells (`INF`).  
The first time we reach a cell, it is guaranteed to be the **shortest distance**.

---

### Algorithm

- Iterate over the grid:
    - Add all treasure cells (`0`) to the queue
- While queue is not empty:
    - Pop current cell `(x, y)`
    - Explore all 4 directions:
        - If neighbor is in bounds and is `INF`:
            - Update distance: `grid[nx][ny] = grid[x][y] + 1`
            - Add neighbor to queue

---

### Implementation

```python
--8<-- "problems/graphs/04-islands-and-treasure/solution.py:islands_and_treasure"
```

### Complexity

- Time: O(m * n) Each cell is visited at most once.
- Space: O(m * n) Queue can hold all cells in worst case.

---

## 4. Edge Cases

- Empty grid → no operation needed
- No treasures (0) → all cells remain INF
- All walls → no changes
- Single cell grid

---

## 5. Pattern Generalization

This problem is an example of:

- Multi-source BFS
- Shortest distance in unweighted grid
- Distance propagation problems

Similar problems:

- Rotting Oranges
- 01 Matrix
- Shortest Path in Binary Matrix

---

## 6. Final Takeaway

> When you need the shortest distance from multiple sources, push all sources into the queue first and run BFS.

Distance spreads outward from all sources simultaneously, and the first time a cell is reached gives the shortest path.
