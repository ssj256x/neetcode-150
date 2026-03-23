## Subsets II

**Difficulty**: Medium  
**Pattern**: Backtracking | Sorting | Duplicate Skipping  
**Link**: https://neetcode.io/problems/subsets-ii/question?list=neetcode150

---

## 1. Problem Summary

Given an integer array `nums` that **may contain duplicates**, return all possible subsets (the power set).

- The solution must **not contain duplicate subsets**
- Return the result in any order

---

## 2. Key Observations

- This is a variation of the **Subsets (Power Set)** problem
- The presence of **duplicates** introduces the challenge of avoiding duplicate subsets
- Sorting helps **group duplicates together**
- We must ensure that duplicates are only considered **once per recursion level**

---

## 3. Approach 1 — Brute Force (Generate + Deduplicate)

### Idea

Generate all possible subsets (including duplicates), then remove duplicates using a set.

---

### Algorithm

1. Generate all subsets using standard backtracking
2. Convert each subset to a sorted tuple
3. Insert into a set to remove duplicates
4. Convert back to list

---

### Complexity

- **Time**: Worse than `O(n * 2^n)` due to duplicate generation + deduplication
- **Space**: Extra space for set → `O(n * 2^n)`

---

### Why It’s Suboptimal

- Generates duplicate subsets unnecessarily
- Extra overhead of hashing and storage
- Not optimal for large inputs

---

## 4. Optimal Approach

### Core Insight

```text
Sort the array and skip duplicates at the same recursion level
```

---

### Structural Transformation

- Sorting groups duplicates together
- Skipping ensures we **don’t explore identical branches**
- We still allow duplicates in deeper recursion to form valid subsets

---

### Algorithm

1. Sort the input array
2. Use backtracking with a `start` index
3. At each recursion:
    - Add current subset to result
    - Iterate from `start` to end:
        - If `i > start` and `nums[i] == nums[i-1]`, skip
        - Include element and recurse
        - Backtrack

---

### Implementation

```python
--8<-- "problems/backtracking/05-subsets-ii/solution.py:subsets_with_dup"
```

---

### Complexity

Let `n = len(nums)`

- **Time**: `O(n * 2^n)`
    - Each element has 2 choices (include/exclude)
    - Copying subset costs `O(n)`

- **Space**:
    - Recursion stack: `O(n)`
    - Output space: `O(n * 2^n)`

---

## 5. Edge Cases

- Empty input → `[[]]`
- Single element → `[[], [x]]`
- All elements same → reduced number of unique subsets
- Negative numbers → no impact
- Large input → exponential growth

---

## 6. Pattern Generalization

This problem is an example of:

- Backtracking with **constraints**
- **Duplicate handling via sorting**
- Controlled recursion to avoid redundant work

---

### Similar problems

- Combination Sum II
- Permutations II
- Subsets (without duplicates)

---

## 7. Final Takeaway

```text
Sort → group duplicates
Skip → duplicates at the same recursion level
Allow → duplicates in deeper recursion
```

> The real lesson is not the solution — it’s the pattern.