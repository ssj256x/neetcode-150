# Recursion — How to Think About It (Not Memorize It)

---

## 1. What Recursion *Really* Is

```text
Recursion = solving a problem by reducing it into smaller versions of itself
```

---

### 🔥 Mental Model

```text
"I will solve this problem from position X,
assuming I know how to solve it from X+1"
```

---

## 2. The Real Question You Should Ask

Instead of:

```text
"How many parameters should I pass?"
```

Ask:

```text
"What information do I need to uniquely define my current situation?"
```

👉 THAT is your **state**

---

## 3. What is “State”?

```text
State = minimal information needed to continue the problem
```

---

### 🟢 Subsets

```text
What do I need?
- Where I am → index
- What I’ve chosen → path
```

```python
(index, path)
```

---

### 🔵 Permutations

```text
What do I need?
- What I’ve used → used[]
- Current arrangement → path
```

```python
(path, used)
```

---

### 🟡 Palindrome Partitioning

```text
What do I need?
- Where to cut next → start
- Current partition → path
```

```python
(start, path)
```

---

### 🔴 Word Search

```text
What do I need?
- Current position → (i, j)
- Progress in word → idx
```

```python
(i, j, idx)
```

---

## 4. Rule for Designing Recursive Function

---

### 🔥 Golden Rule

```text
Parameters = State
```

---

### 💡 Checklist

```text
1. Where am I?           → index / position
2. What have I done?     → path / result
3. What is remaining?    → target / remaining / unused
```

---

## 5. When Should You Use Recursion?

---

### ✅ Use Recursion When:

---

#### 1. Explore all possibilities

```text
subsets, permutations, combinations
```

---

#### 2. Try all paths

```text
DFS, grids, trees
```

---

#### 3. Divide into smaller problems

```text
merge sort, quick sort
```

---

#### 4. Build step-by-step

```text
generate parentheses
```

---

#### 5. Make decisions at each step

```text
include/exclude, pick next, cut here
```

---

## 6. When NOT to Use Recursion

---

### ❌ Avoid when:

```text
- Simple iteration works
- Stack depth can explode
- No branching / no decision tree
```

---

## 7. Base Case — What It REALLY Means

---

Most people think:

```text
Base case = stopping condition
```

Better:

```text
Base case = when the answer is COMPLETE
```

---

### Examples

---

#### Subsets

```python
result.append(path[:])
```

---

#### Permutations

```python
if len(path) == len(nums):
```

---

#### Partitioning

```python
if start == len(s):
```

---

#### Word Search

```python
if idx == len(word):
```

---

## 8. The 3-Step Recursion Thinking

---

### 🔥 Always think in this order:

---

#### 1. Define State

```text
What do I need to know right now?
```

---

#### 2. Define Choices

```text
What can I do from here?
```

---

#### 3. Define Base Case

```text
When am I done?
```

---

## 9. Example (Subsets)

---

### Step 1 — State

```python
(index, path)
```

---

### Step 2 — Choices

```text
Pick next element
```

---

### Step 3 — Base Case

```text
Every path is valid → add anytime
```

---

### Final Code

```python
def backtrack(index, path):
    result.append(path[:])

    for i in range(index, len(nums)):
        path.append(nums[i])
        backtrack(i + 1, path)
        path.pop()
```

---

## 10. Why You Feel Confused

Because you're trying to:

```text
Memorize recursion
```

Instead of:

```text
Model the problem as state + transitions
```

---

## 11. The Fix

```text
Don’t write recursion
Design the STATE first
```

---

## 12. Universal Template

```python
def dfs(state):
    if is_done(state):
        process_result()
        return

    for choice in choices(state):
        if not valid(choice):
            continue

        apply(choice)
        dfs(new_state)
        undo(choice)
```

---

## 🚀 Final Takeaway

```text
Recursion is just:
State → Choices → Base Case
```

---

## 🧠 One-liner

```text
If you can describe "where you are" and "what you can do next",
you can write recursion
```