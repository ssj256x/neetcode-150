# Products of Array Except Self

**Difficulty**: Medium   
**Pattern**: Array | Prefix/Suffix Product
**Link**: https://neetcode.io/problems/products-of-array-discluding-self/question?list=neetcode150

---

## 1. Problem Summary

Given an integer array `nums`, return an array output where `output[i]` is the product of all the elements of `nums`
except `nums[i]`.

```
---
Input: nums = [1, 2, 4, 6]
Output: [48, 24, 12, 8]
---
Input: nums = [-1, 0, 1, 2, 3]
Output: [0, -6, 0, 0, 0]
---
```

The solution must run in `O(n)` time.

---

## 2. Key Observations

- The value at index `i` depends on **all elements except itself**.
- A naive idea is: `product of entire array / nums[i]`

- However this introduces two problems:
    - The problem **disallows division**.
    - Division breaks when the array contains `0`.

Special cases with zeros:

- If there is **1 zero** in the array:
    - Only the index containing `0` will contain the product of the remaining elements.
    - All other indices will be `0`.
- If there are **more than 1 zero**, every element in the result will be `0`.

A key structural observation:

The result for index `i` can be written as:
`product of elements to the left of i × product of elements to the right of i`

This observation leads to the optimal solution.


---

## 3. Approach 1 — Using Total Product (Division Based)

### Idea

Compute the product of all elements and divide by the current element.

We must handle `0` values separately since division by zero is undefined.

### Algorithm

1. Traverse the array and compute:
    - `product` of all non-zero elements
    - `count_zero`
2. If `count_zero > 1`, return an array filled with `0`.
3. If `count_zero == 1`:
    - Return an array of zeros.
    - The index where `nums[i] == 0` should contain the computed `product`.
4. If `count_zero == 0`:
    - Compute `output[i] = product / nums[i]`.

### Complexity

Let `n` be the size of `nums`.

**Time**: `O(n)`
**Space**: `O(n)`

### Why It’s Suboptimal

The problem explicitly requires solving it **without division**.

Additionally, division introduces edge cases when zeros appear in the array.


---

## 3. Approach 1 — Using Total Product (Division Based)

### Idea

Compute the product of all elements and divide by the current element.

We must handle `0` values separately since division by zero is undefined.

### Algorithm

1. Traverse the array and compute:
    - `product` of all non-zero elements
    - `count_zero`
2. If `count_zero > 1`, return an array filled with `0`.
3. If `count_zero == 1`:
    - Return an array of zeros.
    - The index where `nums[i] == 0` should contain the computed `product`.
4. If `count_zero == 0`:
    - Compute `output[i] = product / nums[i]`.

### Complexity

Let `n` be the size of `nums`.

#### Time

`O(n)`

#### Space

`O(n)`

### Why It’s Suboptimal

The problem explicitly requires solving it **without division**.

Additionally, division introduces edge cases when zeros appear in the array.

```text
output[i] = (product of elements before i) × (product of elements after i)
```

We can compute this efficiently using two passes:

- **Prefix product** → product of all elements to the left
- **Suffix product** → product of all elements to the right

This avoids division entirely.

---

### Algorithm

1. Initialize `output` array with size `n`.
2. Traverse the array from left to right:
    - Maintain a running `prefix` product.
    - Store `prefix` in `output[i]`.
3. Traverse the array from right to left:
    - Maintain a running `suffix` product.
    - Multiply `output[i]` with `suffix`.

Example transformation:

```text
nums = [1,2,4,6]

prefix products:
[1,1,2,8]

suffix products:
[48,24,6,1]

result:
[48,24,12,8]
```

---

### Complexity

Let `n` be the size of `nums`.

**Time**

`O(n)` (two linear passes)

**Space**

`O(1)` extra space  
(output array does not count toward extra space)

---

## 5. Edge Cases

- Empty input
- Single element array
- Arrays containing `0`
- Arrays containing multiple `0`s
- Negative numbers
- Large numbers that may cause overflow in some languages

---

## 6. Pattern Generalization

This problem is an example of:

- **Prefix / Suffix accumulation**
- **Precomputing partial results to avoid recomputation**

Instead of recomputing the product for every index (`O(n²)`), we reuse previously computed prefix and suffix
information.

This pattern appears whenever a result depends on: `information to the left + information to the right`

Similar problems:

- **Trapping Rain Water**
- **Range Sum Query**
- **Subarray product / sum queries**

---

## 7. Final Takeaway

The key insight is recognizing that the result for each index can be decomposed into **left and right contributions**.

> The real lesson is not the solution — it’s the pattern.

Whenever a problem requires excluding the current element while aggregating information from the rest of the array,
consider using **prefix and suffix accumulations** to compute results in linear time.