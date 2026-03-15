## Two Sum II — Input Array Is Sorted

**Difficulty**: Medium  
**Pattern**: Two Pointers | Sorted Array  
**Link**: https://neetcode.io/problems/two-integer-sum-ii/question?list=neetcode150

---

## 1. Problem Summary

Given a **1-indexed array of integers `numbers`** that is sorted in **non-decreasing order**, find two numbers such that
they add up to a specific `target`.

Return the **indices of the two numbers (1-indexed)**.

You may assume:

- Exactly **one solution exists**
- The same element **cannot be used twice**
- You must use **constant extra space**

Example 1:

```text
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
```

Explanation:

```
numbers[1] + numbers[2] = 2 + 7 = 9
```

Example 2:

```text
Input: numbers = [1,2,3,4], target = 3
Output: [1,2]
```

---

## 2. Key Observations

The key property of this problem is that the array is **already sorted**.

This allows us to reason about the sum of elements at the ends of the array.

If we place two pointers:

```
numbers = [2,7,11,15]
           ↑      ↑
          left   right
```

We can evaluate:

```
sum = numbers[left] + numbers[right]
```

Three outcomes are possible:

1. If `sum == target` → solution found
2. If `sum < target` → increase the sum by moving `left`
3. If `sum > target` → decrease the sum by moving `right`

Because the array is sorted, moving pointers this way guarantees we eventually find the correct pair.

---

## 3. Approach 1 — Optimal

### Idea

Use the **two-pointer technique**:

- One pointer starts at the **beginning** of the array
- One pointer starts at the **end** of the array

At each step we compare the sum of the elements and adjust the pointers accordingly.

This avoids the need for nested loops.

---

### Algorithm

1. Initialize two pointers:
   ```
   left = 0
   right = len(numbers) - 1
   ```

2. While `left < right`:
    - Compute the sum of the elements at the pointers.
    - If the sum equals the target → return the indices.
    - If the sum is smaller than the target → move `left` forward.
    - If the sum is greater than the target → move `right` backward.

3. If no pair is found return an empty array.

---

### Complexity

Let `n` be the size of the array.

**Time**: `O(n)`

Each pointer moves at most `n` times.

**Space**: `O(1)`

No additional data structures are used.

---

## 4. Edge Cases

- Minimum input size

```
[1,2]
target = 3
```

- Negative numbers

```
[-5,-3,0,4,8]
```

- Large numbers

```
[1000000, 2000000]
```

---

## 6. Pattern Generalization

This problem demonstrates the **Two Pointer on Sorted Array Pattern**.

Key rule:

```
If the array is sorted, two pointers can eliminate the need for nested loops.
```

Instead of checking all pairs in `O(n²)` we move pointers based on whether the current sum is
**too small or too large**.

---

### Similar Problems

- Container With Most Water
- Valid Palindrome
- 3Sum
- 4Sum

---

## 7. Final Takeaway

Whenever a problem involves **pair sums in a sorted array**, the **two-pointer technique** often provides a clean `O(n)`
solution.

> The core insight is that sorting gives us directional information, allowing pointers to move intelligently instead of
> checking every possible pair.