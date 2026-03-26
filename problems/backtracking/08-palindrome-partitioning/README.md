## Palindrome Partitioning

**Difficulty**: Medium  
**Pattern**: Backtracking | String Partitioning | DFS | DP  
**Link**: https://neetcode.io/problems/palindrome-partitioning/question?list=neetcode150  

---

## 1. Problem Summary

Given a string `s`, partition the string such that **every substring** of the partition is a **palindrome**.  
Return **all possible palindrome partitionings** of `s`.

A palindrome is a string that reads the same forward and backward.

---

### Example 1

```text
Input: s = "aab"

Output:
[
  ["a","a","b"],
  ["aa","b"]
]
```

---

### Example 2

```text
Input: s = "banana"

Output:
[
  ["b","a","n","a","n","a"],
  ["b","a","n","ana"],
  ["b","a","nan","a"],
  ["b","ana","n","a"],
  ["b","anana"]
]
```

---

## 2. Key Observations

- This is a **partitioning problem**, not subsets or permutations
- We are **splitting the string into substrings**
- Each substring must satisfy a **constraint → palindrome**
- At every index, we try **all possible substrings starting from that index**
- Only valid (palindrome) substrings are allowed to expand further
- This creates a **decision tree of cuts**

---

## 3. Approach 1 — Backtracking (Brute Force)

---

### Idea

At each index:

- Try every possible substring `s[start:end]`
- If it is a palindrome:
  - Add it to the current path
  - Recurse for the remaining string
- Backtrack and try the next possibility

---

### Algorithm

1. Define recursive function `find(start, path)`
2. If `start == len(s)`:
   - Add current `path` to result
3. Loop `end` from `start → n-1`
4. If `s[start:end+1]` is a palindrome:
   - Add substring to `path`
   - Recurse with `find(end + 1, path)`
   - Backtrack

---

### Implementation

```python title="solution.py"
--8<-- "problems/backtracking/08-palindrome-partitioning/solution.py:partition"
```

---

### Complexity

Let `n` = length of string

#### Time

```
O(n * 2^n)
```

- There are up to `2^n` possible partitions
- Each palindrome check takes `O(n)` in worst case

---

#### Space

```
O(n * 2^n)
```

- Recursion depth = `O(n)`
- Result storage dominates

---

### Why It’s Suboptimal

- Same substrings are checked multiple times for palindrome
- Leads to redundant computation

---

## 4. Approach 2 — Backtracking + Memoization (DP)

---

### Core Insight

Cache the results of palindrome checks:

```text
Avoid recomputing whether s[l:r] is a palindrome
```

---

### Idea

- Use a 2D DP table `dp[l][r]`
  - `None` → not computed
  - `True/False` → cached result
- Before computing palindrome, check if already computed

---

### Algorithm

1. Initialize `dp[n][n]` with `None`
2. Modify `is_palindrome(l, r)`:
   - Return cached value if exists
   - Otherwise compute and store result
3. Use same backtracking logic as before

---

### Implementation

```python title="solution.py"
--8<-- "problems/backtracking/08-palindrome-partitioning/solution.py:partition_dp_mem"
```

---

### Complexity

#### Time

```
O(n * 2^n)
```

- Still explores all partitions
- But palindrome checks are optimized to near `O(1)` amortized

---

#### Space

```
O(n^2 + n * 2^n)
```

- `O(n^2)` for DP table
- Remaining for recursion + results

---

## 5. Edge Cases

- Empty string → `[[]]`
- Single character → always palindrome
- All characters same → maximum branching
- No multi-length palindrome → only single character partitions

---

## 6. Pattern Generalization

This problem is an example of:

- Backtracking (DFS)
- String Partitioning
- Constraint-based recursion
- Memoization (optimization layer)

---

### Similar Problems

- Restore IP Addresses
- Word Break (decision-based partitioning)
- Generate Parentheses (constraint pruning)
- Combination Sum (branch + prune)

---

## 7. Key Pattern Insight

```text
You are not selecting elements,
you are deciding WHERE TO CUT the string
```

---

## 8. Mental Model

```text
At each index:
→ try all possible substrings (cuts)
→ continue only if valid (palindrome)
```

---

## 9. Final Takeaway

```text
Partitioning problems explore all possible cuts,
but prune paths early using constraints
```

---

> The real lesson is not the solution — it’s the pattern.