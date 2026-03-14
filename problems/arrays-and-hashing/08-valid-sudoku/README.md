## Valid Sudoku

**Difficulty**: Medium  
**Pattern**: Array | Hash Table | Matrix
**Link**: https://neetcode.io/problems/valid-sudoku/question?list=neetcode150

---

## 1. Problem Summary

You are given a `9 x 9` Sudoku board `board`. A Sudoku board is valid if the following rules are followed:

- Each row must contain the digits `1-9` without duplicates.
- Each column must contain the digits `1-9` without duplicates.
- Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without duplicates.

Return `true` if the Sudoku board is valid, otherwise return `false`

Note: A board does not need to be full or be solvable to be valid.

---

## 2. Key Observations

- The board size is fixed at `9 x 9`, meaning the total number of cells is constant (`81`).
- Each cell participates in **three independent constraints**:
    - A `row`
    - A `column`
    - A `3 x 3 box`
- If any of these constraints contains a duplicate number, the board becomes invalid.
- Instead of validating rows, columns and boxes separately, we can **track constraint violations while traversing the
  board**.

What structural property makes this solvable?

Every cell belongs to **exactly one row, one column and one box**.  
This allows us to convert the problem into a **constraint tracking problem**.

What structural property makes this solvable?

---

## 3. Approach 1 — Brute Force

### Idea

We iterate all the `rows`, `columns` and `boxes` individually return `False` on finding a duplicate in any of them. Else
we return `True`

> A `Box` is a `3 x 3` square in the sudoku board. There are `9` boxes

### Algorithm

1. Iterate all `rows`, and find unique elements in the row.
2. Iterate all `columns`, and find unique elements in the column.
3. Iterate all `boxes`, and find unique elements in the box.
4. If any iteration hit a duplicate item, return `False`.
5. Return `True` if not duplicates are hit.

### Complexity

The `board` dimensions are fixed at `9 x 9`, and we traverse it `3` times.

We create `9` sets for each traversal, so `27` sets

- **Time**: `3 x O(81)` or `O(1)`
- **Space**: `3 x O(9)` or `O(1)`

### Why It’s Suboptimal

We are traversing the board `3` times. Hence we can do better and traverse only `once`.

---

## 4. Sub-Optimal Approach

### Idea

The previous `Brute Force` idea works but we traverse more than once. But in this approach
we try to traverse only once and maintain `3` separate `sets`.

- `rows[9]` stores a `set` for each `row` to check duplicates.
- `cols[9]` stores a `set` for each `column` to check duplicates.
- `boxes[9]` stores a `set` for each `box` to check duplicates.

> We create an `array` of `sets` because in `Brute Force` implementation we were doing it implicitly.

The `row` and `col` set are fairly straight forward. Its the `box` set that needs special attention.

For a Sudoku Board. The board can be broken down as a `3 x 3` grid of `boxes` where each `box` itself is a `3 x 3` grid.

```text
0 0 0 | 1 1 1 | 2 2 2
0 0 0 | 1 1 1 | 2 2 2
0 0 0 | 1 1 1 | 2 2 2
---------------------
3 3 3 | 4 4 4 | 5 5 5
3 3 3 | 4 4 4 | 5 5 5
3 3 3 | 4 4 4 | 5 5 5
---------------------
6 6 6 | 7 7 7 | 8 8 8
6 6 6 | 7 7 7 | 8 8 8
6 6 6 | 7 7 7 | 8 8 8
```

Hence the board becomes a simple 3 x 3 grid.

```text
0 1 2
3 4 5
6 7 8 
```

We need to map the numbers to these coordinates of `3 x 3` grid.

So the `rows` and `cols` become

```python
row = r // 3  # r is row number [0..8]
col = c // 3  # c is col number [0..8]
```

Now we want to represent this grid as a `1-D Array` which can be done using the formula

```python
# index = row * width + col
i = (r // 3) * 3 + (c // 3)
```

And that is what maps to the `box[9]` set.

---

### Algorithm

1. Traverse the board
2. For each position `continue` if `cur` is `.`
3. Else calculate the `box` index using above formula
4. Then check if the `cur` number is in any of the sets for `rows`, `cols` or `boxes`

---

### Complexity

- **Time**: `O(1)` since we traverse only once
- **Space**: `O(243)` or `O(1)` since we have `27` sets each of max size `9`

---

## 5. Optimal Approach

#### Idea

In the suboptimal approach we use `3 arrays of sets` but we can do it with `1` set only

Instead of adding the `cur` value itself we can add an `entry`

- `row_key = (cur, r)`
- `col_key = (c, cur)`
- `box_key = (r // 3, c // 3, cur)`

Here we insert `3` entries per cell.

> **NOTE**: In python `(0, '5') ≠ ('5', 0)` and we use this property to differentiate between `row` and `col` entries.

A simpler version would be to put the keys as

- `row_key = ('row', cur, r)`
- `col_key = ('col', cur, c)`
- `box_key = ('box', cur, r // 3, c // 3)`

But the first one is compact while still maintaining uniuqness.

#### Algorithm

1. Traverse the board
2. For each position `continue` if `cur` is `.`
3. Generate keys using one of the given approaches
4. Then check if the `keys` are in the `set`

#### Complexity

**Time**: `O(1)` since we traverse only once
**Space**: `O(243)` or `O(1)`

---

## 6. Pattern Generalization

This problem is an example of:

- **Constraint Tracking**
- **Mapping multidimensional constraints into hash keys**

Each element in a grid may participate in multiple independent rules.  
Instead of validating each rule separately, we can **track violations using hash structures while scanning the grid once
**.

This technique appears often in matrix problems where elements must satisfy multiple uniqueness constraints.

Similar problems:

- **N-Queens** (tracking rows, diagonals and anti-diagonals)
- **Word Search / Grid Validation problems**
- **Latin Square validation**

A useful mental model: `value + constraint identifier → unique key`

e.g.

```text
(row, value)
(column, value)
(box, value)
```

If a duplicate key appears, the constraint is violated.

---

## 7. Final Takeaway

Sudoku validation is fundamentally a **constraint tracking problem**.  
Instead of validating rows, columns and boxes separately, we track each constraint using hash structures while scanning
the board once.

> The real lesson is not the solution — it’s the pattern.

Whenever a problem contains **multiple independent uniqueness constraints**, you can convert each constraint into a *
*hashable key** and detect violations in `O(1)` time during traversal.