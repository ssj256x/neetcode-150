# Longest Consecutive Sequence

**Difficulty**: Medium  
**Pattern**: Hash Set | Sequence Detection | Array
**Link**: https://neetcode.io/problems/longest-consecutive-sequence/question?list=neetcode150

---

# 1. Problem Summary

Given an unsorted array of integers `nums`, return the length of the **longest consecutive sequence** of numbers.

A consecutive sequence means each number is exactly **1 greater than the previous number**.

The elements **do not need to appear consecutively in the array**.

You must design an algorithm that runs in **O(n) time**.

```
Input: nums = [2,20,4,10,3,4,5]
Output: 4
Explanation: The longest consecutive sequence is [2,3,4,5]

Input: nums = [0,3,2,5,4,6,1,1]
Output: 7
Explanation: The longest consecutive sequence is [0,1,2,3,4,5,6]
```

---

# 2. Key Observations

### 1. Order in the array does not matter

We only care whether numbers exist.

```
[2,20,4,10,3,4,5]
```

Logically contains

```
2,3,4,5
```

which forms a sequence of length **4**.

---

### 2. Duplicates do not matter

Example

```
[0,3,2,5,4,6,1,1]
```

becomes

```
{0,1,2,3,4,5,6}
```

So duplicates can be ignored.

---

### 3. Fast lookup is required

To check if `n + 1` exists repeatedly, we need **O(1) membership checks**.

A **hash set** provides this.

---

# 3. Brute Force Approach

### Idea

For every number, repeatedly check if the next number exists.

Example

```
2 → 3 → 4 → 5
3 → 4 → 5
4 → 5
```

This recomputes sequences multiple times.

---

### Complexity

Time:

```
O(n²)
```

Space:

```
O(1)
```

---

### Why It’s Suboptimal

Sequences are recomputed multiple times.

Example:

```
2 → 3 → 4 → 5
3 → 4 → 5
4 → 5
```

The same work repeats.

---

# 4. Optimal Approach

## Core Insight

Only start counting a sequence **when you find the beginning of one**.

A number `n` is the **start of a sequence** if:

```
n - 1 NOT in set
```

Example:

```
Set = {2,3,4,5}
```

```
2 → start (1 not present)
3 → skip
4 → skip
5 → skip
```

This guarantees each sequence is processed **once**.

---

# Algorithm

1. Insert all numbers into a **set**.
2. Iterate through each number.
3. If `num - 1` exists in the set, skip.
4. Otherwise, start counting the sequence.
5. Expand while `num + 1` exists.
6. Track the maximum length.

---

# 5. Complexity

Let `n` be the number of elements.

**Time**: `O(n)`

Each number is visited at most twice.

**Space**: `O(n)`

For the hash set.

---

# 6. Edge Cases

### Empty array

```
[] → 0
```

### Single element

```
[5] → 1
```

### Duplicates

```
[1,2,2,3] → 3
```

Duplicates do not affect the result.

---

# 7. Pattern Generalization

This problem demonstrates the pattern:

```
HashSet + Sequence Start Detection
```

Rule:

```
Only start work when the predecessor does not exist
```

This avoids recomputation.

---

# Similar Problems

- Longest Increasing Path (graph variant)
- Consecutive number detection problems
- Sequence expansion problems

---

# 8. Final Takeaway

The key insight is **not to expand sequences from every element**.

Instead, detect **true sequence starting points** using:

```
num - 1 not in set
```

This guarantees each sequence is processed exactly once, enabling an **O(n)** solution.