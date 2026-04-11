## Problem Name

**Difficulty**: Medium  
**Pattern**: Graph | DFS | Topological Sort (Cycle Detection)  
**Link**: <a href="https://neetcode.io/problems/course-schedule/question?list=neetcode150" target="_blank">https://neetcode.io/problems/course-schedule/question?list=neetcode150</a>

---

## 1. Problem Summary

You are given:

- An integer `num_courses`
- A list of prerequisites `prerequisites[i] = [course, pre]`

Each pair indicates:

- To take `course`, you must first complete `pre`

Return `true` if you can finish all courses, otherwise return `false`.

---

## 2. Key Observations

- This is a **dependency graph**
- Each course depends on its prerequisites
- The problem reduces to checking whether a **valid ordering exists**
- A valid ordering exists **iff the graph has no cycles**
- A cycle means:
    - A course depends on itself indirectly
    - Impossible to complete all courses

Hence we apply:

- Directed Graph modeling
- DFS-based cycle detection
- Topological sort validation (implicit)

---

## 3. Approach 1 — Optimal (DFS)

### Idea

We model the courses as a directed graph and use **DFS to detect cycles**.

We maintain a `state` array:

- `0` → unvisited
- `1` → visiting (currently in recursion stack)
- `2` → visited (fully processed)

If during DFS we encounter a node in `visiting` state, it indicates a **cycle**.

---

### Algorithm

- Build adjacency list:
    - `course → prerequisites`
- Initialize `state` array of size `num_courses`
- For each course:
    - If unvisited, run DFS
- In DFS:
    - If node is `visiting` → return `False` (cycle)
    - If node is `visited` → return `True`
    - Mark node as `visiting`
    - Traverse all prerequisites
    - Mark node as `visited`
- If all nodes processed without cycle → return `True`

---

### Implementation

```python title="solution.py"
--8<-- "problems/graphs/08-course-schedule/solution.py:can_finish"
```

---

### Complexity

- **Time**: `O(V + E)` where `V = num_courses`, `E = prerequisites`
- **Space**: `O(V + E)` for graph + recursion stack

---

## 4. Edge Cases

- No prerequisites → return `True`
- Single course → return `True`
- Cycle exists → return `False`
- Disconnected graph → still valid if no cycles
- Self dependency (e.g., `[0,0]`) → return `False`

---

## 5. Pattern Generalization

This problem is an example of:

- Topological Sort (validity check)
- Cycle detection in directed graph
- DFS with recursion stack tracking

Similar problems:

- Course Schedule II (return ordering)
- Alien Dictionary
- Graph Valid Tree (variation)
- Build Order / Dependency Resolution

---

## 6. Final Takeaway

> If a problem involves dependencies and asks whether tasks can be completed, think in terms of **cycles in a directed
graph**.

Use DFS with state tracking (or Kahn’s algorithm) to detect cycles.  
No cycle ⇒ valid topological ordering exists ⇒ all tasks can be completed.