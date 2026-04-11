## Problem Name

**Difficulty**: Medium  
**Pattern**: Graph | Topological Sort | BFS (Kahn’s Algorithm) / DFS  
**Link**: <a href="https://neetcode.io/problems/course-schedule-ii/question?list=neetcode150" target="_blank">https://neetcode.io/problems/course-schedule-ii/question?list=neetcode150</a>

---

## 1. Problem Summary

You are given:

- An integer `num_courses`
- A list of prerequisites `prerequisites[i] = [course, pre]`

Each pair indicates:

- To take `course`, you must first complete `pre`

Return a **valid ordering of courses** such that all prerequisites are satisfied.  
If it is impossible, return an empty list `[]`.

---

## 2. Key Observations

- This is a **dependency graph**
- We are required to **construct a valid order**
- A valid order exists **iff the graph has no cycles**
- Unlike Course Schedule I:
    - We must **return the ordering**, not just validate it
- Multiple valid answers may exist

Hence we apply:

- Topological Sort
- Either:
    - BFS (Kahn’s Algorithm) OR
    - DFS (post-order traversal)

---

## 3. Approach 1 — Optimal (Kahn’s Algorithm / BFS)

### Idea

We process courses that have **no prerequisites first**.

- Track number of dependencies using **indegree**
- Start with all courses having `indegree = 0`
- As we process a course:
    - It “unlocks” dependent courses by reducing their indegree

---

### Algorithm

- Build graph:
    - `pre → course`
- Compute indegree for each course
- Initialize queue with all nodes having `indegree = 0`
- While queue is not empty:
    - Pop node
    - Add to result
    - For each neighbor:
        - Decrement indegree
        - If indegree becomes 0 → add to queue
- If result size == `num_courses` → return result
- Else → return `[]` (cycle exists)

---

### Complexity

- **Time**: `O(V + E)` where `V = num_courses`, `E = prerequisites`
- **Space**: `O(V + E)` for graph + queue

---

### Implementation

```python title="solution.py"
--8<-- "problems/graphs/09-course-schedule-ii/solution.py:find_order"
```

---

## 4. Edge Cases

- No prerequisites → return `[0, 1, ..., n-1]`
- Single course → return `[0]`
- Cycle exists → return `[]`
- Disconnected graph → valid ordering still exists
- Multiple valid answers → any one is acceptable

---

## 5. Pattern Generalization

This problem is an example of:

- Topological Sort (ordering)
- BFS with indegree tracking (Kahn’s Algorithm)
- Dependency resolution

Similar problems:

- Course Schedule I (validation only)
- Alien Dictionary
- Build Order
- Task Scheduling

---

## 6. Final Takeaway

> When asked to return a valid order of tasks with dependencies, use **topological sort**.

Use Kahn’s Algorithm to iteratively process nodes with no dependencies and build the ordering step by step.  
If not all nodes can be processed, a cycle exists and no valid ordering is possible.