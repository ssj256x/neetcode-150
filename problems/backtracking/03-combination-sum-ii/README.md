## Combination Sum II

**Difficulty**: Medium  
**Pattern**: Backtracking | Sorting | Deduplication  
**Link**: https://neetcode.io/problems/combination-target-sum-ii/question?list=neetcode150

---

## 1. Problem Summary

Given an integer array `candidates` of numbers which _can contain duplicate_ numbers, return all possible combinations
where the chosen numbers sum to a given `target`.

- Each element can be chosen **at most once**
- The solution set must **not contain duplicate combinations**
- Return the result in any order

In many backtracking problems (like **Subsets II**, **Combination Sum II**, **Permutations II**), the input array may
contain **duplicate elements**.

The goal is to:

```
Generate unique combinations/subsets/permutations
```

without producing duplicate results.

### Examples

```text
Input: candidates = [9,2,2,4,6,1,5], target = 8

Output: [
  [1,2,5],
  [2,2,4],
  [2,6]
]
```

```text
Input: candidates = [1,2,3,4,5], target = 7

Output: [
  [1,2,4],
  [2,5],
  [3,4]
]
```

---

## 2. Key Observations

### Sorting is the foundation

```python
nums.sort()
```

Why?

```
Sorting groups duplicate elements together
```

Example:

```text
[2,1,2] → [1,2,2]
```

---

### Core Rule for Skipping Duplicates

```python
if i > start and nums[i] == nums[i - 1]:
    continue
```

### Condition Breakdown

```text
i > start
```

→ Ensures we are at the **same recursion level**

```text
nums[i] == nums[i - 1]
```

→ Current element is a duplicate

```text
If this is the same number as previous at the same level → skip it
```

Example:

```text
nums = [1,2,2]
```

### Recursion Tree (without skipping)

```text
        []
      /  |   \
     1   2    2   ❌ duplicate branch
```

### With skipping

```text
        []
      /   \
     1     2
```

Second `2` is skipped at the same level

### Important Subtlety

We ONLY skip at the same level  
We still allow duplicates in deeper recursion.

### Example

```text
nums = [1,2,2]
```

Valid subset:

```text
[2,2] ✅ allowed
```

So:

```text
Skip at same level
Allow at deeper levels
```

---

## 3. Approach - Backtracking (Optimal)

The solution is similar to the **Combination Sum**, we just add the condition

```python
--8<-- "problems/backtracking/03-combination-sum-ii/solution.py:combination_sum_2"
```

### Complexity

If `n` is the size of `candidates` tjen

**Time**: `O(n * 2^n)`, where `O(n)` is for copying the array and `O(2^n)` for exploring all combinations
**Space**: `O(n * 2^n)`, where `O(n)` is the stack depth and `O(2^n)` is for output space

---

## 4. Pattern Generalization

This pattern applies to:

- Subsets II
- Combination Sum II
- Permutations II

---

### Key Difference Across Problems

| Problem                         | Recursion         |
|---------------------------------|-------------------|
| Subsets II                      | `i + 1`           |
| Combination Sum II              | `i + 1`           |
| Combination Sum (reuse allowed) | `i`               |
| Permutations II                 | Use visited array |

---

## 5. Final Takeaway

```text
Sort → group duplicates
Skip → duplicates at same recursion level
Allow → duplicates in deeper recursion if needed
```

---

### 🔥 Golden Rule

```text
if i > start and nums[i] == nums[i - 1]:
    continue
```

> Efficient backtracking is not about filtering duplicates later —  
> it’s about **never generating them in the first place**.