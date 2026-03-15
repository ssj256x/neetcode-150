## Valid Palindrome

**Difficulty**: Easy  
**Pattern**: Two Pointers | String  
**Link**: https://neetcode.io/problems/is-palindrome/question?list=neetcode150

---

## 1. Problem Summary

Given a string `s`, return `true` if it is a **palindrome**, otherwise return `false`.

A **palindrome** is a string that reads the same forward and backward.

The comparison must:

- be **case-insensitive**
- **ignore all non-alphanumeric characters**

**Note:** Alphanumeric characters consist of letters `(A-Z, a-z)` and numbers `(0-9)`.

Example 1:

```text
Input: s = "Was it a car or a cat I saw?"
Output: true
```

Explanation: After filtering non-alphanumeric characters and converting to lowercase we get:

```
wasitacaroracatisaw
```

which reads the same forward and backward.

Example 2:

```text
Input: s = "tab a cat"
Output: false
```

Explanation:

```
tabacat
```

is not a palindrome.

---

## 2. Key Observations

Consider the word:

```
civic
```

If we compare characters from both ends:

```
c i v i c
↑       ↑
```

they are the same.

Move inward:

```
c i v i c
  ↑   ↑
```

again the characters match.

This observation leads to the core idea:

> If characters from the **left and right ends match while moving inward**, the string is a palindrome.

However, the problem introduces two additional constraints:

1. **Ignore non-alphanumeric characters**
2. **Comparison must be case-insensitive**

---

## 3. Approach 1 — Optimal

### Idea

Use the **two-pointer technique**:

- One pointer starts at the **beginning**
- One pointer starts at the **end**

Both pointers move toward the center while comparing characters.

Before comparison:

- Skip **non-alphanumeric characters**
- Convert characters to **lowercase**

If at any point the characters do not match, the string is **not a palindrome**.

---

### Algorithm

1. Define `left = 0` and `right = len(s) - 1`.
2. While `left < right`:
   1. If `s[left]` is **not alphanumeric**, increment `left`.
   2. If `s[right]` is **not alphanumeric**, decrement `right`.
   3. Otherwise:
      - Compare `s[left].lower()` and `s[right].lower()`.
      - If they are not equal → return `False`.
      - If equal → increment `left` and decrement `right`.
3. If the loop completes without mismatches, return `True`.

---

### Complexity

Let `n` be the length of the string.

**Time Complexity**

```
O(n)
```

Each character is visited at most once.

**Space Complexity**

```
O(1)
```

No additional data structures are used.

---

## 4. Edge Cases

- Strings containing **only non-alphanumeric characters**

```
"!!!"
```

Should return:

```
true
```

because the filtered string becomes empty.

- **Single character strings**

```
"a"
```

Always a palindrome.

- **Mixed case letters**

```
"Aa"
```

Should return `true`.

---

## 6. Pattern Generalization

This problem demonstrates the **Two Pointer Symmetry Pattern**.

Core idea:

```
Compare elements from both ends and move inward.
```

This technique is commonly used when:

- validating **symmetry**
- checking **palindromes**
- processing **sorted arrays**
- shrinking a search space from both sides

---

### Similar Problems

- Valid Palindrome II
- Reverse String
- Container With Most Water
- Two Sum II (sorted array variant)

---

## 7. Final Takeaway

When a problem requires comparing elements from **opposite ends of a sequence**, the **two-pointer technique** often leads to an optimal solution with **O(n)** time and **O(1)** space.

> The real lesson is recognizing **symmetry in data** and exploiting it using two pointers.