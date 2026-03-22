## Permutations

**Difficulty**: Medium  
**Pattern**: Backtracking  
**Link**: https://neetcode.io/problems/permutations/question?list=neetcode150

---

## 1. Problem Summary

Given an array `nums` of **unique integers**, return all possible permutations.

- A permutation is an arrangement of elements where **order matters**
- Return the answer in any order

---

### Examples

```text
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

```text
Input: nums = [7]
Output: [[7]]
```

---

## 2. Key Observations

- Unlike subsets:
    - We must use **all elements**
    - The only variation is **ordering**
- At each position, we can pick **any unused element**
- This creates a **factorial growth (n!)** in possibilities

---

## 3. Approach 1 — Backtracking with Visited Array

### Core Idea

Build the permutation step-by-step by choosing elements that have not yet been used.

---

### Algorithm

1. Maintain:
    - `path` → current permutation
    - `used[]` → tracks whether an element is already included

2. At each recursion:
    - If `len(path) == len(nums)`:
        - Add a copy of `path` to result
    - Else:
        - Iterate over all elements
        - Skip if already used
        - Include element → recurse → backtrack

---

### Implementation

```python
--8<-- "problems/backtracking/04-permutations/solution.py:permute_with_seen"
```

---

### Complexity

Let `n = len(nums)`

#### Time

```
O(n * n!)
```

- Total permutations = `n!`
- Each permutation requires `O(n)` to copy

---

#### Space

- Recursion stack: `O(n)`
- Output space: `O(n * n!)`

---

## 4. Approach 2 — Backtracking with In-Place Swapping

### Core Idea

Fix each position by swapping elements instead of tracking usage separately.

---

### Algorithm

1. Start from index `start = 0`
2. For each position:
    - Swap current element with every element from `start → n-1`
    - Recurse for next index
    - Swap back (backtrack)

---

### Implementation

```python
--8<-- "problems/backtracking/04-permutations/solution.py:permute_with_swap"
```

---

### Complexity

#### Time

```
O(n * n!)
```

#### Space

- Recursion stack: `O(n)`
- No extra `used[]` array (in-place)
- Output: `O(n * n!)`

---

## 5. Approach 3 — Bitmask (Alternative to `used[]`)

### Core Idea

Use an integer bitmask to track which elements are already used.

---

### Implementation

```python
def permute(nums: list[int]) -> list[list[int]]:
    result = []
    n = len(nums)

    def backtrack(path, mask):
        if len(path) == n:
            result.append(path.copy())
            return

        for i in range(n):
            if (mask >> i) & 1:
                continue

            path.append(nums[i])
            backtrack(path, mask | (1 << i))
            path.pop()

    backtrack([], 0)
    return result
```

---

### Complexity

Same as other approaches:

```
Time: O(n * n!)
Space: O(n)
```

---

## 6. Why Bitmask Is Not Ideal Here

- Bitmask only tracks **used elements**
- It does not naturally encode **order**
- Adds complexity without real performance benefit

---

## 7. Pattern Generalization

This problem demonstrates:

- Backtracking with **state tracking**
- Generating **all arrangements (permutations)**
- Managing **choices at each position**

---

### Key Pattern Rule

```text
At each step → choose any UNUSED element
```

---

## 8. Comparison with Subsets

| Problem      | Choice          | Growth |
|--------------|-----------------|--------|
| Subsets      | include/exclude | 2^n    |
| Permutations | pick unused     | n!     |

---

## 9. Why is the Time Complexity NOT O(2^n)?

This is a common point of confusion when comparing **subsets** and **permutations**.

---

### Subsets → O(2^n)

In subset problems:

```text
Each element has 2 choices:
- Include
- Exclude
```

So for `n` elements:

```text
2 × 2 × 2 × ... (n times) = 2^n
```

👉 This forms a **binary decision tree**

---

### Permutations → O(n!)

In permutation problems:

```text
We are NOT deciding whether to include elements
We are deciding the ORDER of elements
```

---

### Think in terms of positions

For:

```text
nums = [1,2,3]
```

#### Step 1 (Position 1)

```text
3 choices → [1], [2], [3]
```

#### Step 2 (Position 2)

```text
2 choices left for each branch
```

#### Step 3 (Position 3)

```text
1 choice left
```

---

### Total permutations

```text
3 × 2 × 1 = 3! = 6
```

---

### General Formula

```text
n × (n-1) × (n-2) × ... × 1 = n!
```

---

## Tree Comparison

### Subsets (Binary Tree)

```text
Depth = n
Choices per level = 2

→ Total = 2^n
```

---

### Permutations (Factorial Tree)

```text
Depth = n
Choices per level = n, n-1, ..., 1

→ Total = n!
```

---

## Key Intuition

| Problem Type | Question Being Asked          | Complexity |
|--------------|-------------------------------|------------|
| Subsets      | "Do I take this element?"     | 2^n        |
| Permutations | "What goes in this position?" | n!         |

---

## Final Takeaway

```text
2^n comes from independent binary decisions
n! comes from arranging elements in order
```

---

## 10. Edge Cases

- Single element → return `[nums]`
- Empty input → return `[[]]` (depending on definition)
- Negative numbers → no impact
- Large `n` → factorial explosion

---

## 11. Final Takeaway

```text
Permutations = arranging all elements in every possible order
```

---

### 🔥 Core Insight

```text
Subsets → binary decision
Permutations → multi-choice decision (n choices per level)
```

> Backtracking works best when you clearly define:
> - what choices you have
> - what constraints limit those choices