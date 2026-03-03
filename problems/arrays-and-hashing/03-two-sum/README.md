## Two Sum

**Difficulty**: Easy  
**Pattern**: Arrays | Hash Map | Complement Lookup  
**Link**: https://neetcode.io/problems/two-integer-sum/question?list=neetcode150  

---

## 1. Problem Summary

Given an integer array `nums` and an integer `target`,
return the indices of the two numbers such that they add up to `target`.

Assume exactly one solution exists.

---

## 2. Key Observations

- Order does not matter.
- We need indices, not values.
- Checking every pair works but is inefficient.
- If `a + b = target`, then:
  
  ```
  b = target - a
  ```

This complement relationship is the key insight.

---

## 3. Approach 1 — Brute Force

### Idea

Check all possible pairs of elements and return the pair whose sum equals the target.

### Implementation Logic

- Use two nested loops.
- Compare every pair `(i, j)`.
- Return when a valid sum is found.

### Complexity

- **Time**: O(n²)
- **Space**: O(1)

### When to Use

- Very small inputs
- Quick prototype
- When optimization is not required

---

## 4. Approach 2 — Hash Map (Optimal)

### Core Idea: Complement Lookup

Instead of checking all pairs, we use the complement identity:

```
If nums[i] + nums[j] = target
Then nums[j] = target - nums[i]
```

So while iterating:

- For each number, compute its complement.
- Check if that complement was seen before.
- If yes → solution found.
- Otherwise, store the complement needed for future.

---

### Implementation Strategy

1. Initialize an empty dictionary `lookup`
2. Iterate through the array once
3. If current number exists in `lookup`
   - Return stored index and current index
4. Otherwise
   - Store `target - nums[i]` as key and index as value

---

### Why This Works

The dictionary acts as a memory of:

> "What number do I need to see in the future to complete a valid pair?"

This transforms the problem from:

- Pair comparison (O(n²))

Into:

- Single-pass lookup (O(n))

---

### Complexity

- **Time**: O(n)
- **Space**: O(n)

Space is O(n) because in the worst case,
all elements are stored in the hash map.

---

## 5. When to Use This Pattern

Use complement lookup when:

- You need to find pairs matching a condition
- The condition can be rewritten algebraically
- Fast lookups are needed
- One-pass solutions are possible

Common problems using this pattern:

- Two Sum
- 3Sum (extension)
- Subarray Sum Equals K
- Longest Consecutive Sequence

---

## 6. Comparison of Approaches

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| Brute Force | O(n²) | O(1) | Simple | Slow |
| Hash Map | O(n) | O(n) | Optimal | Extra space |

---

## 7. Core Insight

The real insight is not about iteration.

It is about recognizing that:

> Pair problems can often be reduced to a complement lookup problem.

Instead of searching for two numbers,
search for one number while remembering what its partner should be.

---

## 8. Pattern Classification

This problem belongs to:

- Complement Lookup Pattern
- Hash Map Optimization
- One-Pass Scanning
- Algebraic Reduction

---

## Final Takeaway

The brute force solution solves the problem directly.

The optimal solution solves it intelligently —
by transforming the problem into a lookup problem
using algebra and hashing.