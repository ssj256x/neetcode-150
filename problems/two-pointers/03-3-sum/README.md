## 3Sum

**Difficulty**: Medium  
**Pattern**: Two Pointers | Sorting  
**Link**: https://neetcode.io/problems/three-integer-sum/question?list=neetcode150

---

## 1. Problem Summary

Given an integer array `nums`, return **all unique triplets** `[nums[i], nums[j], nums[k]]` such that:

```
nums[i] + nums[j] + nums[k] == 0
```

Constraints:

- `i`, `j`, and `k` must be **distinct indices**
- The solution set must **not contain duplicate triplets**

Example:

```text
Input: nums = [-1,0,1,2,-1,-4]

Output:
[
  [-1,-1,2],
  [-1,0,1]
]
```

---

## 2. Key Observations

### 1. Brute force approach is expensive

The naive approach would try every combination of three numbers:

```
O(n³)
```

This quickly becomes inefficient for large inputs.

---

### 2. Sorting unlocks structure

If we sort the array:

```
[-1,0,1,2,-1,-4]
```

becomes

```
[-4,-1,-1,0,1,2]
```

Sorting allows us to:

- use **two pointers**
- detect **duplicates easily**

---

### 3. Reduce 3Sum to 2Sum

The key transformation is:

```
nums[i] + nums[j] + nums[k] = 0
```

Rearrange:

```
nums[j] + nums[k] = -nums[i]
```

This means:

- Fix `nums[i]`
- Solve **Two Sum** on the remaining array

---

## 3. Approach 1 — Optimal

### Idea

1. Sort the array.
2. Iterate through the array fixing one number.
3. Use the **two-pointer technique** to find the remaining two numbers.
4. Skip duplicates to ensure unique triplets.

---

### Algorithm

1. Sort the input array.
2. Loop through each index `i`:
    - Skip duplicate values of `nums[i]`.
3. Initialize two pointers:
   ```
   left = i + 1
   right = len(nums) - 1
   ```
4. While `left < right`:
    - Compute the sum of the triplet.
    - If the sum is **less than 0**, move `left` forward.
    - If the sum is **greater than 0**, move `right` backward.
    - If the sum equals **0**:
        - Store the triplet
        - Move both pointers
        - Skip duplicate values.

```python title="solution"
--8<-- "problems/two-pointers/03-3-sum/solution.py"
```

---

## 4. Complexity

Let `n` be the size of the input array.

### Time Complexity

```
Sorting → O(n log n)
Two pointer scan → O(n²)
```

Overall:

```
O(n²)
```

This is the **optimal complexity** for the 3Sum problem.

---

### Space Complexity

```
O(1)
```

Excluding the space used for the output list.

---

## 5. Edge Cases

### All positive numbers

```
[1,2,3,4]
```

No possible triplet → return `[]`.

---

### All negative numbers

```
[-5,-4,-3]
```

Also produces no valid triplet.

---

### Duplicate numbers

```
[-1,-1,-1,2]
```

Should produce:

```
[-1,-1,2]
```

only **once**.

---

## 6. Pattern Generalization

This problem demonstrates the pattern:

```
Fix one element + Two Pointer Search
```

General structure:

```
k-Sum → Fix one element → Solve (k-1)Sum
```

Examples:

- **2Sum** → two pointers
- **3Sum** → fix one element + two pointers
- **4Sum** → fix two elements + two pointers

---

### Similar Problems

- 3Sum Closest
- 4Sum
- Two Sum II (sorted array)
- Container With Most Water

---

## 7. Final Takeaway

The key insight is reducing the problem from **three nested loops** to **one loop plus a two-pointer search**.

Sorting the array provides structure that allows us to move pointers intelligently instead of checking every
combination.

> Many array problems become easier once sorting enables efficient pointer movement.