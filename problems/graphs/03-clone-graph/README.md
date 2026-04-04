## Clone Graph

**Difficulty**: Medium  
**Pattern**: Graph | DFS | BFS | HashMap  
**Link**: <a href="https://neetcode.io/problems/clone-graph?list=neetcode150" target="_blank">https://neetcode.io/problems/clone-graph?list=neetcode150</a>

---

## 1. Problem Summary

You are given a reference to a node in a **connected undirected graph**.

Each node contains:

- A value `val`
- A list of its neighbors

Your task is to return a **deep copy (clone)** of the entire graph.

A deep copy means:

- All nodes must be newly created
- The structure (connections) must be identical
- No node in the cloned graph should reference any node from the original graph

A node is given as

```python title="node.py"
--8<-- "problems/graphs/03-clone-graph/solution.py:node"
```

---

## 2. Key Observations

- This is a **graph traversal problem** (can use DFS or BFS)
- The graph may contain **cycles**
- Without tracking visited nodes, we can end up in **infinite recursion**
- We need a mapping from:

```text
original node → cloned node
```

- This mapping ensures:
- Each node is cloned only once
- Cycles are handled correctly

Hence, we apply:

- DFS or BFS traversal
- HashMap (visited map) for memoization

---

## 3. Approach 1 — Optimal (DFS)

### Idea

Traverse the graph using DFS. For each node:

- If it is already cloned → return the cloned node
- Else:
- Create a new node
- Store it in the map
- Recursively clone its neighbors

---

### Algorithm

- If input node is None → return None
- Initialize a hashmap old_to_new
- Define DFS:
- If node exists in map → return mapped clone
- Create clone node
- Store mapping
- For each neighbor:
- Recursively clone and append to neighbors
- Return cloned version of input node

---

### Implementation

```python title="solution.py"
--8<-- "problems/graphs/03-clone-graph/solution.py:clone_graph_dfs"
```

---

### Complexity

- Time: `O(V + E)` We visit each node and edge once.
- Space: `O(V)` For hashmap and recursion stack.

---

## 4. Approach 2 — BFS

### Idea

Use BFS traversal instead of DFS. The logic remains the same:

- Use a queue
- Clone nodes level by level
- Maintain mapping

---

### Implementation

```python title="solution.py"
--8<-- "problems/graphs/03-clone-graph/solution.py:clone_graph_bfs"
```

---

### Complexity

- Time: `O(V + E)` We visit each node and edge once.
- Space: `O(V)` For hashmap and recursion stack.

---

## 5. Edge Cases

- Input node is None
- Graph with a single node
- Graph with cycles
- Graph where nodes have no neighbors

---

## 6. Pattern Generalization

This problem is an example of:

- Graph traversal with cycle detection
- DFS/BFS with memoization
- Deep copy / cloning problems

Similar problems:

- Copy List with Random Pointer
- Course Schedule (cycle detection)
- Number of Connected Components

---

## 7. Final Takeaway

> When cloning graph-like structures with cycles, always maintain a mapping between original and cloned nodes.

DFS/BFS + HashMap prevents infinite loops and ensures each node is cloned exactly once.