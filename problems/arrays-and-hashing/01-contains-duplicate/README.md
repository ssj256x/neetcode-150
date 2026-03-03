## Contains Duplicate

**Difficulty**: Easy  
**Pattern**: Arrays | Hash Set | Membership Lookup  
**Link**: https://neetcode.io/problems/duplicate-integer/question?list=neetcode150  

---

## 1. Problem Summary

Given an integer array `nums`, return `True` if any value appears at least twice in the array.  
Return `False` if all elements are distinct.

---

## 2. Key Observations

- We do not need indices.
- We do not need counts.
- We only need to know whether a duplicate exists.
- Early termination is possible once a duplicate is found.

---

## 3. Approach — Hash Set (Optimal)

### Core Idea: Membership Tracking

A set allows O(1) average-time membership checks.

While iterating:
- If a number has already been seen → duplicate found.
- Otherwise, store it in the set.

---

### Implementation Strategy

1. Initialize an empty set `seen`
2. Iterate through each number in the array
3. If the number exists in `seen`
   - Return `True`
4. Otherwise
   - Add the number to `seen`
5. If loop completes → return `False`

---

### Why This Works

A set guarantees uniqueness.

The moment we attempt to insert a value that already exists,
we know a duplicate has been found.

This avoids:
- Sorting
- Nested loops
- Explicit counting

---

### Complexity

- **Time**: O(n)  
  Each lookup and insertion is O(1) on average.

- **Space**: O(n)  
  In the worst case (all unique elements), the set stores all values.

---

## 4. Alternate Approaches

### 1️⃣ Sorting

- Sort the array
- Check adjacent elements for equality

**Time**: O(n log n)  
**Space**: O(1) (if sorting in place)

Not optimal because sorting is unnecessary for simple duplicate detection.

---

### 2️⃣ Brute Force (Nested Loops)

- Compare every pair of elements

**Time**: O(n²)  
**Space**: O(1)

Inefficient for large inputs.

---

## 5. When to Use This Pattern

Use a set when:

- You need fast membership checks
- You need uniqueness enforcement
- You need early termination on duplicates
- Order does not matter

Common problems using this pattern:

- Contains Duplicate
- Happy Number
- Longest Consecutive Sequence
- Detect cycle in linked list (conceptually similar tracking idea)

---

## 6. Pattern Classification

This problem belongs to:

- Hashing
- Membership Lookup
- Early Exit Optimization
- Set-Based Deduplication

---

## 7. Core Insight

The key realization is:

> When the task is to detect duplicates, the problem reduces to fast membership checking.

A set transforms the problem from a comparison problem into a lookup problem.

---

## Final Takeaway

Instead of comparing elements against each other,
store what you've seen and detect repetition immediately.

When the question is about duplicates,
think: **Set**.