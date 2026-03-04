# Top K Frequent Elements

**Difficulty**: Medium  
**Pattern**: Hashing | Array | Heap (Priority Queue) | Sorting  
**Link**: https://neetcode.io/problems/top-k-elements-in-list/question?list=neetcode150

---

## 1. Problem Summary

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements in the array.

- The answer can be returned in any order.
- You may assume `k` is valid (`1 ≤ k ≤ number of unique elements`).

---

## 2. Key Observations

- Since we need frequency, we must count occurrences of each number.
- Since we need the top `k`, we need ordering based on the frequency.
- Full sorting may not be necessary because we only care about the top `k`, not all elements.

---

## 3. Approach 1 — Sorting by Frequency

### Core Idea

1. Count the frequency of each number.
2. Sort the numbers by frequency in descending order.
3. Pick the first `k` elements.

This is straightforward and easy to implement.

---

### Algorithm

1. Initialize empty dictionary `freq`
2. For each number:
    - If not seen, insert with count 1
    - Else increment count
3. Sort the dictionary items by frequency in descending order
4. Extract first `k` elements (only the numbers)

---

### Complexity

Let:

- `n` = number of elements in `nums`
- `m` = number of unique elements

#### Time

- Building frequency dictionary → O(n)
- Sorting by frequency → O(m log m)

Final:

```
O(n + m log m)
```

Worst case (m ≈ n):

```
O(n log n)
```

#### Space

- Frequency dictionary → O(m)

Worst case:

```
O(n)
```

---

## 4. Approach 2 — Using Heap (Optimal)

### Core Insight

We do not need full sorting.

We only need the top `k` most frequent elements, so we can maintain a structure that only keeps the best `k` candidates.

This is where a min-heap of size `k` becomes powerful.

Instead of sorting all `m` elements:

- Push each `(frequency, number)` into a min-heap
- If heap size exceeds `k`, remove the smallest frequency

This ensures:

The heap always contains the `k` most frequent elements seen so far.

---

### Algorithm

1. Build frequency dictionary `freq`
2. Initialize empty min-heap
3. For each `(number, count)` in `freq`:
    - Push `(count, number)` into heap
    - If heap size > `k`, pop the smallest element
4. Extract numbers from heap and return them

---

### Why Convert to Tuple?

We push elements as:

```
(count, number)
```

Because Python’s heap compares elements lexicographically:

- First compares `count`
- If counts are equal, compares `number`

This allows the heap to:

- Automatically organize elements by frequency
- Keep the smallest frequency at the top

Tuples are immutable and comparable, making them ideal for heap usage.

---

### Complexity

Let:

- `n` = total elements
- `m` = unique elements

#### Time

- Building frequency map → O(n)
- Heap operations → O(m log k)

Final:

```
O(n + m log k)
```

Worst case (m ≈ n):

```
O(n log k)
```

If `k << n`, this is significantly faster than sorting.

#### Space

- Frequency dictionary → O(m)
- Heap → O(k)

Total:

```
O(m)
```

Worst case:

```
O(n)
```

---

## 5. Comparison

| Approach | Time       | Space | When to Use                   |
|----------|------------|-------|-------------------------------|
| Sorting  | O(n log n) | O(n)  | Simple implementation         |
| Heap     | O(n log k) | O(n)  | When k is much smaller than n |

### Why Heap Is Better

Sorting orders all elements.

Heap maintains only k elements.

If:

n = 1,000,000  
k = 10

Sorting → ~20 million operations  
Heap → ~3 million operations

Huge improvement.

---

## 6. Pattern Generalization

### “Top K” Pattern

Whenever you see:

- Top K largest
- Top K smallest
- K most frequent
- K closest points

Think:

- Min-heap of size K (for largest problems)
- Max-heap of size K (for smallest problems)

---

### Frequency Counting Pattern

Whenever the problem involves:

- Duplicates
- Frequency comparison
- Most/least frequent elements

Think:

`Dictionary` / `HashMap`

---

## 7. Interview Insight

In interviews:

1. Start with sorting (simple and correct).
2. Then say:

> We can optimize this by using a min-heap of size k since we only need the top k elements.

This demonstrates:

- Optimization thinking
- Understanding of heap usage
- Awareness of time complexity tradeoffs

---

## Final Takeaway

This problem teaches two major concepts:

1. Frequency counting using HashMap
2. Partial ordering using Heap

Key optimization idea:

We don’t need full sorting.
We only need the top k elements.

Which improves complexity from:

```
O(n log n)
```

to

```
O(n log k)
```

When `k` is small relative to `n`, the heap solution is significantly more efficient and more scalable.