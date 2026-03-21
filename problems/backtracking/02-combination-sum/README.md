## Combination Sum

**Difficulty**: Medium  
**Pattern**: Backtracking | Pruning  
**Link**: https://neetcode.io/problems/combination-target-sum/question?list=neetcode150

---

## 1. Problem Summary

Given an integer array `nums` of **unique elements**, return all possible combinations where the chosen numbers sum to a
given `target`.

- You may use the **same element multiple times**
- The solution set must **not contain duplicate combinations**
- Return the result in any order

---

### Examples

```text
Input:
nums = [2,5,6,9]
target = 9

Output:
[[2,2,5],[9]]
```

```text
Input:
nums = [3,4,5]
target = 16

Output:
[[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]
```

```text
Input:
nums = [3]
target = 5

Output:
[]
```

---

## 2. Key Observations

- This is a **constrained subset generation** problem
- We are not interested in all subsets — only those where:

```
sum == target
```

- Each element has two choices:
    - Include it
    - Skip it

- Unlike subsets:
    - We can **reuse elements multiple times**
    - So recursion does **not always move forward**

---

## 3. Approach 1 — Backtracking (Basic)

### Core Idea

Explore all possible combinations by trying every number and reducing the remaining target.

---

### Algorithm

1. Start with:
   ```
   path = []
   remaining = target
   ```

2. At each recursion:

- If `remaining == 0`:
    - Add current path to result

- If `remaining < 0`:
    - Stop exploring this path

3. Iterate from current index:

- Include `nums[i]`
- Recurse with:
  ```
  remaining - nums[i]
  ```
- Stay at same index (`i`) → allows reuse
- Backtrack after recursion

---

### Implementation

```python title="solution.py"
--8<-- "problems/backtracking/02-combination-sum/solution.py:combination_sum"
```

---

### Complexity

Let:

- `n` = number of elements
- `T` = target
- `m` = minimum value in `nums`

#### Time

```
O(n^(T / m))
```

- Worst case: repeatedly picking smallest element
- Depth ≈ `T / m`
- Each level has up to `n` choices

---

#### Space

```
O(T / m)
```

- Recursion stack depth

Output space:

```
O(k * L)
```

---

### Drawback

- Explores unnecessary branches
- No early stopping within loop

---

## 4. Approach 2 — Optimized (Backtracking + Sorting + Pruning)

### Core Idea

Sort the array so that we can **stop early** when elements exceed the remaining target.

---

### Key Optimization

```python
if nums[i] > remaining:
    break
```

---

### Why This Works

After sorting:

```
nums = [2,3,5,7]
```

If:

```
nums[i] > remaining
```

Then:

```
nums[i+1], nums[i+2] ... will also be > remaining
```

So:

```
No valid combination possible → stop loop
```

---

### Algorithm

1. Sort the array
2. Use backtracking
3. At each step:
    - If `remaining == 0` → add result
    - Iterate from `start`
    - If `nums[i] > remaining` → **break**
    - Include element and recurse
    - Backtrack

---

### Implementation

```python title="solution.py"
--8<-- "problems/backtracking/02-combination-sum/solution.py:combination_sum_with_sort"
```

---

### Complexity (Optimized)

#### Time

```
O(n^(T / m))  (worst case)
```

- Same theoretical upper bound
- But **much faster in practice due to pruning**

---

#### Space

```
O(T / m)
```

- Recursion stack depth

Output:

```
O(k * L)
```

---

## 5. Why Sorting + Pruning Matters

### Without sorting

```python
if nums[i] > remaining:
    continue
```

- Still checks all elements
- Cannot stop early

---

### With sorting

```python
if nums[i] > remaining:
    break
```

- Skips entire remaining loop
- Avoids exploring useless branches

---

## 6. Pattern Generalization

This problem demonstrates:

- Backtracking with **constraints**
- Backtracking with **pruning**
- Combination generation with **repetition allowed**

---

### Key Rule

| Scenario      | Recursion               |
|---------------|:------------------------|
| Reuse allowed | `backtrack(i, ...)`     |
| No reuse      | `backtrack(i + 1, ...)` |

---

## 7. Related Problems

- Combination Sum II (no reuse, duplicates in input)
- Combination Sum III (fixed size)
- Subsets
- Permutations
- Partition problems

---

## 8. Final Takeaway

```text
Backtracking explores possibilities
Pruning eliminates impossible paths early
Sorting enables stronger pruning
```

> Efficient backtracking is not about exploring everything — it’s about knowing what NOT to explore.