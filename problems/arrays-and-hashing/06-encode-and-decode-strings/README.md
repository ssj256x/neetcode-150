# Encode and Decode Strings

**Difficulty**: Medium  
**Pattern**: Array | String | Design  
**Link**: https://neetcode.io/problems/string-encode-and-decode/question?list=neetcode150

---

## 1. Problem Summary

Design an algorithm to encode a list of strings into a single string such that it can be transmitted over a network and
later decoded back into the original list of strings.

You must implement two functions:

- `encode(strs)` → converts a list of strings into a single encoded string
- `decode(s)` → reconstructs the original list of strings from the encoded string

The decoded list must exactly match the original list.

---

## 2. Key Observations

- Strings may contain **any characters**, including punctuation or delimiters.
- Therefore we **cannot safely split using a delimiter** like `,` or `|`.
- Instead, we must encode enough information so that decoding is **unambiguous**.
- The safest approach is to store the **length of each string before the string itself**.

---

## 3. Approach

### Core Idea

Each string is encoded as: `length#string`

Example:

```python
strs = ["red", "black", "purple", "white"]
encoded = "3#red5#black6#purple5#white"
```

The decoder can:

1. Read digits until `#`
2. Convert to integer length
3. Extract exactly that many characters
4. Continue parsing the remainder of the string

Because we rely on **length instead of delimiters**, the solution works even if the string contains special characters.


---

### Algorithm

### Encode

1. Initialize an empty list `encoded`
2. For each string `s` in `strs`:
    - Compute `len(s)`
    - Append `"length#string"` to `encoded`
3. Join all pieces into a single string
4. Return the encoded string

---

### Decode

1. Initialize pointer `i = 0`
2. While `i < len(encoded_string)`:
    - Move pointer `j` until `#` is found
    - Extract substring `encoded[i:j]` and convert to integer `length`
    - Extract next `length` characters
    - Add extracted string to result list
    - Move pointer forward to continue parsing
3. Return result list

---

### Complexity

Let:

- `n` = number of strings
- `m` = total number of characters across all strings

#### Time

Encoding: `O(m)`

Decoding:`O(m)`

#### Space

Encoding: `O(m)`

Decoding:`O(m)`


---

## 6. Pattern Generalization

This problem represents the concept of serialization and deserialization.

Common uses include:
- Network communication
- File storage formats
- Message queues
- Distributed systems

The key principle is:
> Data must be encoded in a reversible and unambiguous format.

---

## 7. Interview Insight

Interviewers want to see whether you recognize that:

- Delimiter-based splitting is unsafe
- The encoding must be reversible

The main insight is:
> Use a length prefix to guarantee unambiguous decoding.
---

## Final Takeaway

The important idea is not the parsing logic but the encoding design.

By prefixing each string with its length: `length#string` we ensure the encoded data can always be decoded correctly,
regardless of the characters contained within the original strings.