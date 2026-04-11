# 🧠 Problem Solving Patterns — DFS, BFS, Backtracking

---

## 🚀 1. High-Level Decision Tree

When you see a problem, start with this:

---

### 🔍 What is the problem asking?

---

#### 🟩 A. Explore regions / connected components

- Traverse the grid or graph
- Find clusters / components

👉 Use:
- DFS (preferred)
- BFS (also valid)

**Examples:**
- Number of Islands
- Max Area of Island
- Word Search

---

#### 🟦 B. Minimum steps / shortest time / nearest distance

👉 Use:
- BFS

**Why?**
- BFS explores level-by-level → guarantees shortest path in unweighted graphs

**Examples:**
- Rotting Oranges
- 01 Matrix
- Islands & Treasure

---

#### 🟥 C. Multiple sources spreading simultaneously

👉 Use:
- Multi-Source BFS

**Key Idea:**
- All sources start at the same time
- Spread happens in "waves"

**Examples:**
- Rotting Oranges
- Islands & Treasure

---

#### 🟪 D. Reach boundary / ocean / escape

👉 Use:
- Reverse DFS/BFS (start from boundary)

**Key Idea:**
- Instead of checking from every cell → start from destination

**Examples:**
- Pacific Atlantic Water Flow
- Surrounded Regions

---

#### 🟨 E. Generate all combinations / paths

👉 Use:
- Backtracking

**Examples:**
- Permutations
- Subsets
- Generate Parentheses
- Palindrome Partitioning
- Letter Combinations

---

## 🌳 2. Mermaid Decision Diagram

```mermaid
flowchart TD
    A[Start: Analyze Problem]
    A --> B{What is being asked?}
%% --- Exploration ---
    B -->|Explore regions / components| C[DFS or BFS]
    C --> C1[Number of Islands]
    C --> C2[Max Area of Island]
    C --> C3[Word Search]
%% --- Shortest Path ---
    B -->|Minimum steps / time| D[BFS]
    D --> D1[Rotting Oranges]
    D --> D2[01 Matrix]
    D --> D3[Islands & Treasure]
%% --- Multi Source ---
    B -->|Multiple sources spreading| E[Multi-Source BFS]
    E --> E1[Rotting Oranges]
    E --> E2[Islands & Treasure]
%% --- Boundary / Reverse ---
    B -->|Reach boundary / ocean| F[Reverse DFS/BFS]
    F --> F1[Pacific Atlantic]
    F --> F2[Surrounded Regions]
%% --- Backtracking ---
    B -->|All combinations / paths| G[Backtracking]
    G --> G1[Permutations]
    G --> G2[Subsets]
    G --> G3[Generate Parentheses]
    G --> G4[Palindrome Partitioning]
    G --> G5[Letter Combinations]
%% --- DFS vs BFS decision ---
    C --> H{Need shortest path?}
    H -->|Yes| D
    H -->|No| I[DFS Preferred]
%% --- Core Pattern Layer ---
    subgraph Patterns
        P1[DFS = Explore]
        P2[BFS = Shortest Path]
        P3[Multi-Source BFS = Spread]
        P4[Reverse Traversal = Boundary Reachability]
        P5[Backtracking = Generate]
    end
```