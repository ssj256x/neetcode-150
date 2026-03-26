## Letter Combinations of a Phone Number

**Difficulty**: Medium  
**Pattern**: Backtracking | Combinatorial Generation  
**Link**: https://neetcode.io/problems/combinations-of-a-phone-number/question?list=neetcode150

---

## 1. Problem Summary

Given a string `digits` containing digits from `2-9`, return all possible letter combinations that the number could
represent based on the mapping of digits to letters on a telephone keypad.

Each digit maps to a set of characters:

```text
2 → abc
3 → def
4 → ghi
5 → jkl
6 → mno
7 → pqrs
8 → tuv
9 → wxyz
```

---

### Example 1

```text
Input: digits = "23"

Output:
["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

---

### Example 2

```text
Input: digits = "594"

Output:
All combinations formed by:
5 → jkl
9 → wxyz
4 → ghi
```

---

## 2. Key Observations

- Each digit contributes a **set of possible characters**
- The final result is a **combination of one character per digit**
- This is equivalent to computing a **Cartesian product of character sets**
- We build the result **one character at a time**
- The length of each valid combination is exactly `len(digits)`

---

## 3. Approach — Backtracking

---

### Idea

- Start from index `0`
- For each digit, iterate over its mapped characters
- Append a character to the current string
- Recurse for the next digit
- Backtrack and try the next character

---

### Algorithm

1. If `digits` is empty, return `[]`
2. Define a recursive function `generate(idx, s)`
3. If `len(s) == len(digits)`:
    - Add the built string to result
4. Loop `i` from `idx` to `len(digits) - 1`
5. For each character mapped to `digits[i]`:
    - Append character to `s`
    - Recurse with `generate(i + 1, s)`
    - Backtrack by removing last character

---

### Implementation

```python title="solution.py"
--8<-- "problems/backtracking/09-letter-combinations-of-a-phone-number/solution.py:letter_combinations"
```

---

## 4. Complexity

Let `n = len(digits)`  
Let `k = average number of letters per digit (≈ 3 to 4)`

---

### Time

```
O(k^n)
```

- At each position, we branch into up to `k` choices
- Total combinations = `k * k * ... (n times)`

---

### Space

```
O(n * k^n)
```

- `O(n)` recursion depth
- `O(k^n)` to store all combinations

---

## 5. Edge Cases

- Empty input → return `[]`
- Single digit → return all mapped characters
- Digits with 4 mappings (`7`, `9`) → slightly higher branching

---

## 6. Pattern Generalization

This problem is an example of:

- Backtracking (DFS)
- Combinatorial generation
- Cartesian product construction

---

### Similar Problems

- Generate Parentheses
- Subsets
- Combination Sum
- Permutations

---

## 7. Key Insight

```text
At each digit, pick one character and move forward
```

---

## 8. Mental Model

```text
Build the string one character at a time,
choosing from the available letters of each digit
```

---

## 9. Important Note

```text
Unlike permutations:
- No need for visited[]
- Each position has fixed choices
```

---

## 10. Final Takeaway

```text
This problem is about building combinations across fixed groups,
one level at a time using backtracking
```

---

> The real lesson is not the solution — it’s the pattern.