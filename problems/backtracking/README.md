# ↩️ Backtracking Template (Reusable)

This is the gold template you’ll reuse for:

- Subsets
- Combinations
- Permutations
- Combination Sum
- N-Queens
- etc.

---

## 🧠 Generic Template

```python
def backtrack(start, path):
    # 1. Add current state if valid
    result.append(path.copy())

    # 2. Explore choices
    for i in range(start, len(nums)):
        # choose
        path.append(nums[i])

        # explore
        backtrack(i + 1, path)

        # un-choose
        path.pop()
```

Example with [**Subsets**](https://leetcode.com/problems/subsets/description/) problem:

```python
def subsets(nums: list[int]) -> list[list[int]]:
    result = []

    def backtrack(start: int, path: list[int]):
        result.append(path.copy())

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result
```

---

## 🔄 Template Variations (VERY IMPORTANT)

You don’t always use **start** the same way.

### 🔹 1. Subsets (No reuse)

```python
backtrack(i + 1)
```

### 🔹 2. Combination Sum (Reuse allowed)

```python
backtrack(i)
```

### 🔹 3. Permutations (Use visited)

```python
if used[i]:
    continue
```

### 🔹 4. Fixed Length (k combinations)

```python
if len(path) == k:
    result.append(path.copy())
    return
```

---

## 🧠 Mental Model

```text
Backtracking = DFS over decision tree
```

Every problem becomes:

1. Define state (path)
2. Define choices (loop)
3. Define constraints (pruning)
4. Undo choice

---

## 🔥 Final Takeaway

**Iterative**:

- Build layer by layer
- Easier to write

**Backtracking**:

- Explore tree depth-first
- More powerful & general

