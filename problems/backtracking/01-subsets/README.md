## Subsets (Power Set)

**Difficulty**: Medium  
**Pattern**: Backtracking | Bit Manipulation  
**Link**: https://neetcode.io/problems/subsets/question?list=neetcode150

---

## 1. Problem Summary

Given an integer array `nums` of **unique elements**, return all possible subsets (the power set).

- The solution set must **not contain duplicate subsets**
- The result can be returned in **any order**

---

### Examples

```text
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

```text
Input: nums = [0]
Output: [[],[0]]
```

---

## 2. Key Observations

### 1. Total number of subsets

For `n` elements:

```
Total subsets = 2^n
```

---

### 2. Binary decision per element

Each element has two choices:

```
Include it
Exclude it
```

This naturally forms a **decision tree**.

---

### 3. Every state is a valid subset

Unlike many backtracking problems:

```
Every intermediate path is a valid answer
```

---

## 3. Approach 1 — Backtracking (Optimal & General)

### Core Idea

Traverse the **decision tree** and collect all subsets during traversal.

---

### Algorithm

1. Start with an empty subset.
2. At each recursion:
   - Add current subset to result.
   - Iterate through remaining elements.
   - Include current element.
   - Recurse.
   - Backtrack (remove element).

---

### Implementation

```python
--8<-- "problems/backtracking/01-subsets/solution.py:solution_backtracking"
```

---

### Complexity

- **Time**: `O(n * 2^n)`
- **Space**: `O(n)` (recursion stack)
- Output space: `O(n * 2^n)`

---

### Why This Approach is Powerful

- Works for **all subset-type problems**
- Easy to extend with:
  - constraints
  - pruning
  - conditions

---

## 4. Approach 2 — Bitmasking (Iterative)

### Core Idea

Each subset corresponds to a **binary number** from `0` to `2^n - 1`.

Each bit represents whether an element is included.

---

### Example

```text
nums = [1,2,3]

mask    binary    subset
0       000       []
1       001       [3]
2       010       [2]
3       011       [2,3]
4       100       [1]
5       101       [1,3]
6       110       [1,2]
7       111       [1,2,3]
```

---

### Algorithm

1. Loop from `0 → 2^n - 1`
2. For each number:
   - Check each bit position
   - If bit is set, include corresponding element

---

### Implementation

```python
--8<-- "problems/backtracking/01-subsets/solution.py:solution_xor"
```

---

### Complexity

- **Time**: `O(n * 2^n)`
- **Space**: `O(n * 2^n)`

---

## 5. Comparison of Approaches

| Aspect | Backtracking | Bitmask |
|------|-------------|--------|
| Strategy | DFS decision tree | Binary representation |
| Readability | High | Medium |
| Flexibility | Very high | Low |
| Extensibility | Easy | Hard |
| Recursion | Yes | No |
| Best use case | General problems | Simple subset generation |

---

## 6. Pros & Cons

### Backtracking

#### Pros

- Very intuitive
- Matches problem structure
- Easily extendable
- Works with constraints and pruning

#### Cons

- Slightly more verbose
- Recursion overhead

---

### Bitmasking

#### Pros

- Compact and concise
- No recursion
- Easy to implement once understood

#### Cons

- Less intuitive
- Hard to extend for complex problems
- Not suitable for constraint-based variations

---

## 7. Pattern Generalization

This problem demonstrates the **Subset / Decision Tree Pattern**.

General form:

```
At each element → choose or skip
```

---

### Related Problems

- Subsets II (with duplicates)
- Combination Sum
- Permutations
- Partition problems

---

## 8. Final Takeaway

Backtracking explores the **decision tree**, while bitmasking uses **binary representation** to generate subsets.

```text
Backtracking = Conceptual & extensible
Bitmasking = Compact & mathematical
```

> Master backtracking first — bitmasking becomes intuitive afterward.