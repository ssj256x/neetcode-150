## Valid Anagram

**Difficulty**: Easy  
**Pattern**: Arrays | Frequency Counting | Hashing  
**Link**: https://neetcode.io/problems/is-anagram/question?list=neetcode150  

---

## 1. Problem Summary

Given two strings `s` and `t`, determine whether `t` is an anagram of `s`.

Two strings are anagrams if they contain the same characters with the same frequencies, regardless of order.

---

## 2. Key Observations

- If the lengths differ → they cannot be anagrams.
- Order of characters does not matter.
- Frequency of each character must match exactly.
- Input consists of lowercase English letters ('a'–'z').

---

## 3. Approach 1 — Sorting

### Idea

If two strings are anagrams, sorting both strings should produce identical sequences.

### Implementation Logic

1. Sort `s`
2. Sort `t`
3. Compare the results

### Complexity

- **Time**: O(n log n)
- **Space**: O(n)

### When to Use

- When input constraints are small
- When simplicity is preferred over optimal performance

---

## 4. Approach 2 — Frequency Balancing (Optimal)

### Core Idea: Frequency Balancing

Instead of sorting, treat a fixed-size array as a frequency scale:

- String `s` deposits counts into buckets
- String `t` withdraws counts from the same buckets
- If perfectly balanced → all buckets end at zero

---

### Implementation Strategy

1. If lengths differ → return `False`
2. Create `lookup[26]` initialized with zeros
3. For each character in `s`, increment its bucket
4. For each character in `t`, decrement its bucket
5. If all values in `lookup` are zero → strings are anagrams

---

### Indexing Trick

We map characters to array indices using:

```
ord(c) - ord('a')
```

This maps:
- 'a' → 0  
- 'b' → 1  
- ...  
- 'z' → 25  

This avoids hashing and ensures O(1) access with a very small constant factor.

---

### Complexity

- **Time**: O(n)
- **Space**: O(1)

Why O(1) space?

Because the lookup array is fixed at size 26, independent of input size.

---

## 5. When to Use This Pattern

Use frequency balancing when:

- Order does not matter
- Character/domain size is small and fixed
- Need linear time complexity
- Comparing frequency equality

Common problems:
- Valid Anagram
- Permutation checks
- Sliding Window character problems
- Finding duplicates in constrained domains

---

## 6. Comparison of Approaches

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| Sorting | O(n log n) | O(n) | Simple | Slower |
| Frequency Array | O(n) | O(1) | Optimal | Requires fixed character domain |

---

## 7. Core Insight

The real insight is recognizing that:

> When order doesn't matter, frequency comparison is often more efficient than sorting.

This transforms the problem from a comparison problem into a counting problem.

---

## 8. Pattern Classification

This problem belongs to:

- Frequency Counting
- Fixed-Size Hashing
- Constant Space Optimization
- Array Index Mapping

---

## Final Takeaway

The optimal solution is not about comparing strings —
it's about balancing frequency counts efficiently using a fixed-size structure.