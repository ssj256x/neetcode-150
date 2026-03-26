# Backtracking — Unified Template & Pattern Recognition

---

## 1. Unified Backtracking Template

This is the **core template** behind:

- Subsets
- Permutations
- Combination Sum
- Palindrome Partitioning
- Generate Parenthesis
- N-Queens

---

### 🧠 Master Template

```python
def backtrack(state, path):
    # 1. Base case
    if is_complete(state):
        result.append(path[:])
        return

    # 2. Iterate choices
    for choice in get_choices(state):

        # 3. Constraint check (PRUNING)
        if not is_valid(choice, state):
            continue

        # 4. Choose
        apply(choice, state, path)

        # 5. Explore
        backtrack(state, path)

        # 6. Undo (BACKTRACK)
        undo(choice, state, path)
```

---

### 🧠 What changes per problem?

| Part          | Meaning                            |
|---------------|------------------------------------|
| `state`       | index / used[] / remaining target  |
| `path`        | current solution                   |
| `choices`     | elements / substrings / directions |
| `is_valid`    | constraints                        |
| `is_complete` | stopping condition                 |

---

## 2. Pattern Specializations

---

### 🟢 A. Subsets

```python
def backtrack(index, path):
    result.append(path[:])

    for i in range(index, len(nums)):
        path.append(nums[i])
        backtrack(i + 1, path)
        path.pop()
```

#### Pattern

```text
Choose next element or skip
```

---

### 🔵 B. Permutations

```python
def backtrack(path):
    if len(path) == len(nums):
        result.append(path[:])
        return

    for i in range(len(nums)):
        if used[i]:
            continue

        used[i] = True
        path.append(nums[i])

        backtrack(path)

        path.pop()
        used[i] = False
```

#### Pattern

```text
Pick unused element
```

---

### 🟡 C. Palindrome Partitioning

```python
def backtrack(start, path):
    if start == len(s):
        result.append(path[:])
        return

    for end in range(start, len(s)):
        if is_palindrome(start, end):
            path.append(s[start:end + 1])
            backtrack(end + 1, path)
            path.pop()
```

#### Pattern

```text
Try all substring cuts
```

---

### 🔴 D. Generate Parentheses

```python
def backtrack(s, open, close):
    if len(s) == 2 * n:
        result.append(s)
        return

    if open < n:
        backtrack(s + "(", open + 1, close)

    if close < open:
        backtrack(s + ")", open, close + 1)
```

#### Pattern

```text
Build valid sequence with constraints
```

---

## 3. Decision Tree (Interview Gold)

---

### 🧠 Step 1 — What is being asked?

---

#### ❓ “All subsets / combinations”

👉 Use:

```text
SUBSETS PATTERN
```

---

#### ❓ “All permutations / arrangements”

👉 Use:

```text
PERMUTATION PATTERN
```

---

#### ❓ “Split string / partition”

👉 Use:

```text
PARTITIONING PATTERN
```

---

#### ❓ “Generate valid sequences”

👉 Use:

```text
CONSTRAINED BACKTRACKING
```

---

## 4. Step 2 — Ask THIS question

```text
What am I choosing?
```

---

### If answer is:

---

#### 🟢 “Elements”

```text
→ Subsets / Combination Sum
```

---

#### 🔵 “Positions / order”

```text
→ Permutations
```

---

#### 🟡 “Cuts / substrings”

```text
→ Partitioning
```

---

#### 🔴 “Valid structure”

```text
→ Constraint-based (Parenthesis, N-Queens)
```

---

## 5. Step 3 — Identify State

---

| Pattern         | State            |
|-----------------|------------------|
| Subsets         | index            |
| Permutations    | used[]           |
| Partitioning    | start index      |
| Combination Sum | remaining target |
| Grid DFS        | i, j             |

---

## 6. Cheat Sheet

---

### 🟢 Subsets

```text
Binary decision
Include / skip
```

---

### 🔵 Permutations

```text
Pick any unused element
```

---

### 🟡 Partitioning

```text
Try all substrings from current index
```

---

### 🔴 Constrained

```text
Only build valid paths
```

---

## 7. Mental Shortcut

When stuck, ask:

```text
Am I:
1. Picking elements?
2. Arranging elements?
3. Cutting string?
4. Building valid structure?
```

---

## 8. Final Takeaway

```text
Backtracking is not 10 patterns
It is ONE template applied differently
```

---

## 🧠 One-liner

```text
Identify what you're choosing → the pattern becomes obvious
```