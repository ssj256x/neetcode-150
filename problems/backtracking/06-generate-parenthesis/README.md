## Generate Parenthesis

**Difficulty**: Medium  
**Pattern**: Backtracking | Constrained Generation | Recursion  
**Link**: https://neetcode.io/problems/generate-parentheses/question?list=neetcode150

---

## 1. Problem Summary

You are given an integer `n`. Return all well-formed parentheses strings that you can generate with `n` pairs of
parentheses.

A string is considered **well-formed** if:

- Every opening bracket `(` has a corresponding closing bracket `)`
- At no point should closing brackets exceed opening brackets

```text
Input: n = 1
Output: ["()"]
```

```text
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

---

## 2. Key Observations

- Unlike subsets or permutations, we **do not generate all possibilities**
- We **only build valid sequences** by enforcing constraints during generation
- The total length of any valid string is always `2 * n`
- At any point:
    - We can add `(` if `open < n`
    - We can add `)` only if `close < open`
- This ensures:
    - We never create invalid intermediate states
    - We avoid unnecessary exploration (pruning)

---

## 3. Approach 1 — Optimal (Backtracking)

### Idea

We build the string step-by-step while maintaining constraints:

- Track:
    - `open` → number of `(` used
    - `close` → number of `)` used
- Only allow moves that keep the string valid

---

### Algorithm

1. Start with an empty string
2. At each step:
    - If length of string is `2 * n`, add to result
    - If `open < n`, add `(` and recurse
    - If `close < open`, add `)` and recurse
3. Backtrack after each recursive call

---

### Implementation

```python title="solution.py"
--8<-- "problems/backtracking/06-generate-parenthesis/solution.py:generate_parenthesis"
```

---

### Complexity

Let `C(n)` be the nth [Catalan number](https://cp-algorithms.com/combinatorics/catalan-numbers.html)

- **Time**: `O(C(n)) ≈ O(4^n / √n)`
    - We generate only valid sequences
- **Space**:
    - Recursion stack: `O(n)`
    - Output space: `O(C(n) * n)`

---

## 4. Why Not O(2^(2n))?

Although each position seems to have 2 choices (`(` or `)`), the constraints eliminate invalid paths early.

```text
We do NOT explore all combinations
We only explore valid states
```

The number of valid combinations is given by the **Catalan Number**:

```text
C(n) = (1 / (n+1)) * (2n choose n)
```

---

## 5. Edge Cases

- `n = 0` → `[""]` (empty string is valid)
- `n = 1` → `["()"]`
- Large `n` → exponential growth in results
- Negative `n` → typically invalid input (can return empty list)

---

## 6. Pattern Generalization

This problem is an example of:

- Backtracking with **constraints**
- **Pruning invalid paths early**
- Generating **valid structures instead of all combinations**

---

### Similar problems

- Valid IP Addresses
- Palindrome Partitioning
- N-Queens
- Expression Add Operators

---

## 7. Final Takeaway

```text
Do not generate all possibilities and filter
Generate only valid solutions by enforcing constraints early
```

> The real lesson is not the solution — it’s the pattern.