## Problem Name

**Difficulty**: Medium    
**Pattern**: Graph | BFS | Multi Source BFS  
**Link**: <a href="https://neetcode.io/problems/rotting-fruit/question?list=neetcode150" target="_blank">https://neetcode.io/problems/rotting-fruit/question?list=neetcode150</a>

---

## 1. Problem Summary

You are given a 2-D matrix `grid`. Each cell can have one of three possible values:

- `0` representing an empty cell
- `1` representing a fresh fruit
- `2` representing a rotten fruit

Every minute, any fresh fruit that is **horizontally or vertically adjacent** to a rotten fruit becomes rotten.

Return the **minimum number of minutes** that must elapse until there are no fresh fruits remaining. If this is
impossible, return `-1`.

---

## 2. Key Observations

- Multiple rotten fruits can spread rot **simultaneously**
- This is not a single-source problem — there are **multiple starting points**
- BFS naturally models **level-by-level (minute-by-minute)** spread
- Each BFS level corresponds to **one minute**
- We must process the grid in **waves**, not individually per cell

Hence we apply:

- Multi-source BFS
- Level-based traversal (time tracking)

---

## 3. Approach 1 — Optimal

### Idea

Instead of running BFS from each rotten fruit independently, we push **all rotten fruits into the queue initially** and
run a **single BFS**. This allows the rotting process to spread simultaneously.

We process BFS **level by level**, where each level represents **one minute**.

---

### Algorithm

- Iterate over the grid:
    - Add all rotten fruits (`2`) to the queue
    - Count total fresh fruits (`1`)
- While queue is not empty and fresh fruits > 0:
    - Process one level:
        - `for _ in range(len(queue))`
        - Pop current cell `(x, y)`
        - Explore all 4 directions:
            - If neighbor is in bounds and is a fresh fruit:
                - Mark it rotten: `grid[nx][ny] = 2`
                - Decrement fresh count
                - Add it to queue
    - Increment time by `1`
- If all fresh fruits are rotten → return `time`
- Else → return `-1`

### Implementation

```python title="solution.py"
--8<-- "problems/graphs/06-rotting-fruit/solution.py:oranges_rotting"
```

### Complexity

- **Time**: `O(n * m)` Since we traverse the board only twice
- **Space**: `O(n * m)` n the worst case, the queue may contain all cells

---

## 4. Edge Cases

- Empty grid → return 0
- No fresh fruits initially → return 0
- Fresh fruits exist but no rotten fruits → return -1
- Isolated fresh fruits (blocked by 0s) → return -1

---

## 5. Pattern Generalization

This problem is an example of:

- Multi-source BFS
- Level-order traversal (time simulation)
- Shortest distance / minimum steps in an unweighted grid

Similar problems:

- Walls and Gates (Islands and Treasure)
- 01 Matrix
- Shortest Path in Binary Matrix

---

## 6. Final Takeaway

> When multiple sources spread simultaneously and you are asked for minimum time or distance, use multi-source BFS with
> level tracking.

Push all sources into the queue first, then expand level by level — each level = one unit of time.