# Group Anagrams

**Difficulty**: Medium  
**Pattern**: Hashing | Frequency Encoding  
**Source**: LeetCode / NeetCode  

---

## 1. Problem Summary

Given an array of strings `strs`, group the anagrams together.

Two strings are anagrams if they contain the same characters with the same frequencies.

Return the grouped anagrams in any order.

---

## 2. Key Observations

- Anagrams are defined by character frequency, not order.
- If two strings contain the same characters in different order,
  they must belong to the same group.
- We need a way to generate a unique signature for each anagram group.

---

## 3. Approach 1 — Sorting as Key

### Core Idea

Sort each string alphabetically.

All anagrams produce the same sorted result.

Example:

```
"cat"  → "act"
"tac"  → "act"
```

Both map to the same dictionary key.

---

### Algorithm

1. Initialize empty dictionary `lookup`
2. For each string:
   - Sort it
   - Use sorted string as key
   - Append original string to that key
3. Return dictionary values

---

### Complexity

Let:
- `n` = number of strings
- `m` = maximum string length

**Time**:  
Sorting each string costs `O(m log m)`  
Done for `n` strings:

```
O(n m log m)
```

**Space**:

```
O(n m)
```

We store all strings and keys.

---

## 4. Approach 2 — Frequency Count (Optimal)

### Core Insight

Sorting is unnecessary.

Anagrams are fully determined by their character frequency distribution.

Since input consists of lowercase letters:

- Alphabet size is fixed (26)
- We can count letters instead of sorting

---

### Algorithm

1. Initialize empty dictionary `lookup`
2. For each string:
   - Create frequency array of size 26
   - Convert it to a tuple
   - Use tuple as dictionary key
3. Append string to corresponding group
4. Return grouped values

---

### Why Convert to Tuple?

- Lists are mutable and unhashable
- Dictionary keys must be hashable
- Tuple is immutable and hashable
- Therefore safe to use as key

---

### Complexity

Counting each string costs `O(m)`

Done for `n` strings:

```
O(n m)
```

Space remains:

```
O(n m)
```

This removes the log factor from sorting.

---

## 5. Comparison

| Approach | Time | Space | Notes |
|----------|------|--------|--------|
| Sorting Key | O(n m log m) | O(n m) | Simpler |
| Frequency Key | O(n m) | O(n m) | Optimal |

---

## 6. Pattern Generalization

This problem demonstrates:

- Hash-based grouping
- Structural encoding
- Using immutable representations as keys
- Eliminating unnecessary sorting

Similar problems:

- Valid Anagram
- Find All Anagrams in a String
- Permutation in String

---

## 7. Interview Insight

If alphabet size is fixed → use frequency counting.

If alphabet size is large or Unicode → sorting may be simpler.

State this explicitly during interviews.

---

## Final Takeaway

The key realization is:

> Anagrams are defined by character frequency, not character order.

Sorting works.

Frequency encoding works better.