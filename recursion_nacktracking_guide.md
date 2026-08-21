# Recursion & Backtracking — The General Formula

A reusable mental model + code skeleton for solving *any* recursion or backtracking problem (Striver A2Z, LeetCode, etc).

---

## 1. The Recursion Mindset

Every recursive function is built from exactly two parts:

```python
def solve(state):
    if base_condition(state):      # 1. BASE CASE — when to stop
        return base_result

    result = combine(solve(smaller_state))   # 2. RECURSIVE CASE
    return result
```

**Trick:** don't try to trace the whole call stack in your head. Just trust that `solve(smaller_state)` already gives the correct answer for the smaller version (this is called the "leap of faith"). Your only job is to figure out how to build the current answer *using* that trusted smaller answer.

---

## 2. The Universal Backtracking Template

Backtracking = recursion + explicitly undoing a choice after exploring it. Use it whenever you're **building something incrementally** (a path, a subset, a board) and need to explore multiple possibilities.

```python
def backtrack(path, state):
    if is_goal(path, state):
        result.append(path[:])     # ALWAYS copy, never store the reference
        return                      # or `return True` if you only need ONE answer

    for choice in get_choices(state):
        if not is_valid(choice, state):
            continue                # pruning — skip invalid branches early

        make_choice(choice, state)  # CHOOSE
        backtrack(path + [choice], state)   # EXPLORE
        undo_choice(choice, state)  # UN-CHOOSE (the "backtrack" step)
```

**Variant — stop at the first valid answer** (used in Sudoku Solver):

```python
def backtrack(state):
    if is_goal(state):
        return True
    for choice in get_choices(state):
        if is_valid(choice, state):
            make_choice(choice, state)
            if backtrack(state):
                return True          # short-circuit — found one, stop everything
            undo_choice(choice, state)
    return False
```

---

## 3. The 5 Questions to Ask For ANY Problem

Before writing a single line of code, answer these:

| # | Question | Example (Rat in a Maze) |
|---|----------|--------------------------|
| 1 | What is my **state**? | current cell `(r, c)` + path so far |
| 2 | What are my **choices** at each state? | 4 directions: D, L, R, U |
| 3 | What makes a choice **invalid**? (pruning) | out of bounds, blocked cell, already visited |
| 4 | What is my **goal / base case**? | reached `(n-1, n-1)` |
| 5 | Do I need **ALL** solutions or just **ONE**? | all → keep looping; one → return early |

If you can answer these 5 in plain English first, the code almost writes itself.

---

## 4. Pattern Library

Most backtracking problems fall into one of these five shapes.

### Pattern A — Include / Exclude (Subsets, Combination Sum)
At each element, decide: take it or skip it.
```python
def backtrack(i, path):
    if i == n:
        result.append(path[:])
        return
    backtrack(i + 1, path)              # exclude arr[i]
    path.append(arr[i])
    backtrack(i + 1, path)              # include arr[i]
    path.pop()
```

### Pattern B — Permutations (order matters, use each element once)
```python
def backtrack(path, used):
    if len(path) == n:
        result.append(path[:])
        return
    for i in range(n):
        if not used[i]:
            used[i] = True
            path.append(arr[i])
            backtrack(path, used)
            path.pop()
            used[i] = False
```

### Pattern C — Grid / Maze Traversal (Rat in a Maze, Word Search)
```python
def backtrack(r, c, path):
    if (r, c) == goal:
        result.append(path)
        return
    for dr, dc, ch in directions:       # e.g. [(1,0,'D'), (0,-1,'L'), (0,1,'R'), (-1,0,'U')]
        nr, nc = r + dr, c + dc
        if isSafe(nr, nc):
            visited[nr][nc] = True
            backtrack(nr, nc, path + ch)
            visited[nr][nc] = False
```

### Pattern D — Board Filling with Constraints (Sudoku, N-Queens)
```python
def backtrack():
    cell = find_next_empty()
    if cell is None:
        return True                     # board fully filled correctly
    r, c = cell
    for val in candidates:
        if isValid(r, c, val):
            place(r, c, val)
            if backtrack():
                return True
            remove(r, c)                 # undo
    return False
```

### Pattern E — Partitioning a String (Palindrome Partitioning)
```python
def backtrack(start, path):
    if start == len(s):
        result.append(path[:])
        return
    for end in range(start + 1, len(s) + 1):
        piece = s[start:end]
        if is_valid_piece(piece):
            path.append(piece)
            backtrack(end, path)
            path.pop()
```

---

## 5. Backtracking vs DP — How to Know Which One You Need

Pure backtracking explores *every* branch — fine when you need **all answers** (all subsets, all paths). But if a problem only asks **"is it possible?" / "how many ways?" / "min/max"**, the *same state* often gets revisited from different paths — that's wasted work.

**The test:** if you called `solve(same_state)` from two different paths, would you get the *same* answer both times?
- **Yes** → the state doesn't care how you got there → memoize it (turn backtracking into DP).
- **No** (you actually need the path itself, or history matters) → pure backtracking, no memo.

This is exactly why **Word Break** looks like Pattern E (partitioning) but becomes DP: we only need `True/False` per starting index, and `dp[i]` means the same thing no matter which earlier split got us to index `i`. Sudoku and Rat-in-a-Maze don't get this treatment because either the *specific* board state matters (Sudoku, many different partial boards) or we need every distinct path (Rat in a Maze).

---

## 6. Debugging Checklist (the bugs that get everyone)

- [ ] Saving `path[:]` (a copy) into `result`, not `path` itself — otherwise later `pop()`s mutate saved answers.
- [ ] The **undo step exactly reverses** the choose step (same variable, same cell).
- [ ] Base case is actually reachable — check for off-by-one on index/size (`i == n` vs `i == n - 1`).
- [ ] Direction/choice order matches the order the problem expects in output (e.g. alphabetical D-L-R-U).
- [ ] Grid problems: mark `visited` **before** recursing, unmark **after** — otherwise infinite loops.
- [ ] Pruning check (`isValid`) happens **before** you recurse, not after — saves huge amounts of wasted work.

---

## 7. Quick Reference

| Problem type | Choice per step | Base case |
|---|---|---|
| Subsets / Combination Sum | include or exclude element | reached end of array |
| Permutations | pick an unused element | path length == n |
| Maze / Word Search | move in a direction | reached target cell |
| Sudoku / N-Queens | place a value in next empty slot | no empty slots left |
| Palindrome Partition | cut string at position `j` | reached end of string |

Same skeleton works in C++/Java too — just swap `path.append/pop()` for `push_back()/pop_back()` (C++) or manual list add/remove (Java); the choose → explore → un-choose structure is identical.
