## Container With Most Water

**Difficulty**: Medium  
**Pattern**: Two Pointers | Greedy  
**Link**: https://neetcode.io/problems/max-water-container/question?list=neetcode150

---

## 1. Problem Summary

You are given an integer array `height` of length `n`. Each element represents the height of a vertical line drawn on
the x-axis.

Two lines together with the x-axis form a **container** that can hold water.

Return the **maximum amount of water** a container can store.

The amount of water is determined by:

```text
area = min(height[left], height[right]) * (right - left)
```

Example:

```text
Input:
height = [1,7,2,5,4,7,3,6]

Output:
36
```

---

## 2. Visual Representation

For the array:

```text
height = [1,7,2,5,4,7,3,6]
index     0 1 2 3 4 5 6 7
```

ASCII elevation diagram:

```text
7 |   █       █
6 |   █       █   █
5 |   █   █   █   █
4 |   █   █ █ █   █
3 |   █   █ █ █ █ █
2 |   █ █ █ █ █ █ █
1 | █ █ █ █ █ █ █ █
   -----------------
    0 1 2 3 4 5 6 7
```

Heights per index:

```text
0 → 1
1 → 7
2 → 2
3 → 5
4 → 4
5 → 7
6 → 3
7 → 6
```

Example container using indices **1 and 7**:

```text
height[1] = 7
height[7] = 6
width = 7 - 1 = 6
water = min(7,6) * 6 = 36
```

Visual:

```text
7 |   █_______█____  ^
6 |   █       █   █  |
5 |   █   █   █   █  |
4 |   █   █ █ █   █  6
3 |   █   █ █ █ █ █  |
2 |   █ █ █ █ █ █ █  |
1 | █ █ █ █ █ █ █ █  |
   ----------------- v
    0 1 2 3 4 5 6 7
      <-----6----->
```

---

## 3. Key Observations

### 1. Container area depends on two things

```text
width = right - left
height = min(height[left], height[right])
```

The water level cannot exceed the **shorter line**.

---

### 2. Brute force approach

Try every pair of lines:

```python
for i in range(n):
    for j in range(i + 1, n):
        # compute area
```

Time complexity: `O(n²)`

This becomes inefficient for large inputs.

---

### 3. Insight for optimization

If we start with the **widest container**:

```
left = 0
right = n - 1
```

The width is maximal.

To potentially increase area we must try to increase the **minimum height**.

Therefore:

```text
move the pointer with the smaller height
```

This is the key insight behind the optimal solution.

---

## 4. Approach 1 — Optimal (Two Pointers)

### Idea

1. Place one pointer at the beginning and one at the end.
2. Compute the area formed by these two lines.
3. Track the maximum area seen so far.
4. Move the pointer that has the **smaller height**.
5. Continue until the pointers meet.

---

### Algorithm

1. Initialize two pointers:

```text
left = 0
right = len(height) - 1
```

2. Initialize `max_area = 0`.

3. While `left < right`:

- Compute area:

```text
area = min(height[left], height[right]) * (right - left)
```

- Update max area.
- Move the pointer pointing to the **smaller height**.

4. Return `max_area`.

---

## 5. Complexity

Let `n` be the number of lines.

**Time**: `O(n)` Since we scan the array only once.
**Space**: `O(1)` Since no extra memory is used.

---

## 6. Edge Cases

### Minimum input size

```text
height = [1,1]
```

Area = `1`.

---

### Strictly increasing heights

```text
[1,2,3,4,5]
```

Best container may not use the tallest line due to width limitations.

---

### Strictly decreasing heights

```text
[5,4,3,2,1]
```

Algorithm still works since it always moves the smaller pointer.

---

## 7. Pattern Generalization

This problem demonstrates the **Two Pointer Greedy Pattern**.

Key idea:

```text
Start with the widest possible container
and shrink the search space intelligently.
```

Important insight:

```text
The shorter line always limits the container height.
```

Therefore moving the taller line cannot improve the result.

---

### Similar Problems

- Two Sum II (sorted array)
- Trapping Rain Water
- 3Sum
- 3Sum Closest

---

## 8. Final Takeaway

Instead of checking every pair of lines, the optimal solution starts with the **widest container** and greedily moves
the pointer limiting the height.

By always discarding the shorter line, we eliminate impossible candidates while preserving the possibility of finding a
larger area.

> The power of the two-pointer technique lies in shrinking the search space without losing optimal solutions.