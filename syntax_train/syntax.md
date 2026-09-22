# syntax.md

Everything looked up or got wrong on 21–22 Sep 2026, across the list/string/dict drills and
LC 1, 217, 49, 3, 560. Read before a round. Written by Claude from the session record —
**strike any line you now know cold, and reword the rest in your own words**; a line you
didn't write is a line you'll re-look-up.

---

## 1. Cost of operations — the one that keeps costing time

| O(1) amortised | O(n) |
|---|---|
| `lst.append(x)`, `lst.pop()`, `lst[i]`, `len(lst)` | `lst.insert(0,x)`, `lst.pop(0)`, `del lst[0]`, `lst.remove(x)` |
| `x in set`, `x in dict`, `d[k]`, `set.add` | `x in lst`, `lst.index(x)`, `lst.count(x)`, **any slice** |

- **`x in lst` is a scan, `x in set` is a hash lookup.** Same syntax, different order. Inside
  a loop that is the difference between O(n) and O(n²). (217, twice.)
- **A slice is a copy.** `lst[1:]` allocates. Recursing with `lst[1:]` is O(n²); pass indices.
- `.index()` / `.count()` inside a loop → O(n²), *and* `.index()` returns the first match, so
  duplicates give wrong answers, not just slow ones.
- `s.count(c)` is one linear scan. Calling it per distinct character to build a table is
  O(n·k) — use `Counter(s)`.
- `bisect.insort` searches in O(log n) but inserts in O(n). Wanting a sorted list you keep
  inserting into is usually the signal for a heap.
- **String `+=` in a loop is O(n²)** — strings are immutable, each concat copies. `join` is O(n).

### Constraints tell you the required complexity — do this before writing anything

Python does roughly 10⁷ simple operations per second.

| n ≤ 20 | n ≤ 500 | n ≤ 5,000 | n ≤ 10⁵ | n ≥ 10⁶ |
|---|---|---|---|---|
| O(2ⁿ) | O(n³) | O(n²) | O(n log n) | O(n) |

**On TLE: stop editing.** TLE is a verdict about the order, not the constant. `while`→`for`
buys ~20%; 560 needed 2,830×.

### The ritual
After writing any loop, say the cost of each call *inside* it, then multiply.
`for n in uniq: nums.count(n)` → "n × O(n) = n², too slow."

---

## 2. Lists

```python
lst.index(x)   lst.count(x)   lst.remove(x)       # methods: type-specific
len  sum  max  min  sorted  enumerate  zip  any  all   # functions: work on any iterable

sorted(lst)            # new list        lst.sort()       # in place, returns None
lst[::-1]              # reversed copy   — NOT sorted(reverse=True), that sorts
lst[-3:]               # last three      lst[:-3] is everything EXCEPT the last three
lst[::2]               # every second    — slices select positions, never transform values

[x*x for x in lst if x % 2]          # expr maps, if filters
[x for row in nested for x in row]   # flatten: outer loop first
list(zip(a, b))                      # stops at the shorter one
```

**Mutators return `None`:** `sort, insert, append, extend, reverse, remove`.
`x = lst.sort()` is `None`. Copy first: `c = lst.copy()` (or `lst[:]`), then mutate `c`.

```python
c[0], c[-1] = c[-1], c[0]     # swap, no temp — RHS fully evaluated before any assignment
lst[:] = [...]                # replace contents IN PLACE (caller sees it)
lst = [...]                   # only rebinds your local name
```

- Indexing raises (`IndexError`), slicing doesn't (`lst[99:]` → `[]`).
- `if not lst:` for empty, not `len(lst) == 0`. And `if lst[i]:` is False when `lst[i]` is 0.
- Don't remove from a list you're iterating — the index shifts under you.
- `[[0]*n]*m` aliases rows. `*` is safe only for immutables. Use `[[0]*n for _ in range(m)]`.

---

## 3. Strings

```python
s.split()          # splits on ANY run of whitespace, drops empties   <- usually what you want
s.split(" ")       # splits on each single space, keeps empties: 'a  b' -> ['a','','b']
sep.join(words)    # string method; separator on the LEFT
s.replace(" ", "") # strings are immutable, so replace-with-empty IS the delete
s[::-1]            # slicing works on strings too
''.join(sorted(w)) # sorted() returns a LIST of chars — this is the anagram key
```

```python
s.find(sub)          # first index, or -1        s.rfind(sub)   # last index
s.index(sub)         # same, but raises ValueError when absent
s.find(sub, start)   # bounded search (str methods are POSITIONAL-ONLY: no start=)
```

**`-1` is a valid index.** `s[s.find('cat')]` silently returns the last character. Compare to
-1 before using the result. Lists have `.index()` but no `.find()`.

```python
ord('a') == 97      ord(c) - ord('a')        # alphabet position, 0..25
chr(ord('a') + i)                            # back to a letter
string.ascii_lowercase                       # 'abc...z', for iterating the alphabet
```

26-slot count array — O(k) anagram key, vs O(k log k) for sorting:

```python
counts = [0]*26
for c in word: counts[ord(c) - ord('a')] += 1
key = tuple(counts)
```

- `isalnum / isalpha / isdigit / isspace` are **whole-string** and False on `''`.
  `all(c.isalnum() for c in s)` differs from `s.isalnum()` on exactly the empty string.
- `endswith` / `startswith` already return bools — `return s.endswith(x)`, never
  `if …: return True / return False`. (And it's `False`, capital F.)
- f-strings: `f"{sub} at {s.find(sub)}"`, `f"{x:.2f}"`, `f"{x=}"` for debugging.
- **Summing `ord()` values does not test anagrams** — `'ad'` and `'bc'` both sum to 197.
  Use `Counter(a) == Counter(b)` or the 26-slot array.
- `'Z' < 'a'` is True (90 < 97) — hence `key=str.lower` for case-insensitive sorts.

---

## 4. Dicts

```python
d.get(k, 0)             # value or default, no KeyError
d[k] = d.get(k, 0) + 1  # the counting idiom — replaces four lines of if/else
d.pop(k, default)       # remove and return, or default
d.setdefault(k, []).append(x)    # one-off defaultdict
k in d                  # O(1) HASH LOOKUP, not iteration
```

**`if d.get(k):` is not a membership test** — it tests the value's truthiness, so a key
holding `0`, `None`, `''` or `[]` reads as missing. Use `k in d`.

| Operation | when key missing |
|---|---|
| `d[k]`, `del d[k]`, `d.pop(k)` | **KeyError** |
| `d.get(k)` | `None` |
| `d.get(k, x)`, `d.pop(k, x)` | `x` |
| `k in d` | `False` |
| `defaultdict(f)[k]` | **creates** `f()`, stores it, returns it |

```python
{k: v*2 for k, v in d.items()}          # comprehension — don't mutate the input
{v: k for k, v in d.items()}            # invert (duplicate values collapse)
sorted(d.items(), key=lambda kv: kv[1], reverse=True)
max(d, key=d.get)                       # returns the KEY with the largest value
Counter(items).most_common(2)
{**a, **b}   or   a | b                 # merge, right wins
dict.fromkeys(lst)                      # dedupe, preserving first-seen order
```

- **Mutating a dict while looping over it raises** `RuntimeError: dictionary changed size`.
  Iterate `list(d)` instead.
- **Reading a missing key from a `defaultdict` creates it** — a later `in` test then lies.
  Use `.get()` on a defaultdict when you only want to look.
- Keys must be hashable: tuples yes, lists no. Hence `tuple(sorted(w))` and `(r, c)` in a
  visited set.

### `key=` — what it does and doesn't do

`key=` changes **what is compared**, never **what comes out**. The iterable you choose
decides the output:

```python
max(d, key=d.get)                       # -> 'a'        (a key)
max(d.items(), key=lambda kv: kv[1])    # -> ('a', 3)   (a pair)
sorted(d, key=d.get)                    # -> keys, in value order
```

The key function must match the element type: iterating `d` gives keys (so `d.get` fits),
iterating `d.items()` gives tuples (so `kv[1]`). Mixing them gives `None` for every element
and a TypeError on comparison.

`key=` belongs to functions that **order or select** and return the originals — `sorted`,
`sort`, `max`, `min`, `nlargest/nsmallest`, `groupby`. Functions that **consume** values —
`sum`, `any`, `all`, `join` — have no `key=`; pass a generator instead: `sum(v for v in … )`.

---

## 5. lambda

One expression, no statements; a ternary is allowed. Only ever passed inline.

```python
sorted(pairs, key=lambda kv: kv[1])
sorted(words, key=lambda w: (-len(w), w))   # length desc, then alphabetical — negate what you can
max(pts, key=lambda p: p[0]**2 + p[1]**2)   # no sqrt needed
defaultdict(lambda: -1)                     # zero-arg factory
sorted(nums, key=cmp_to_key(lambda a, b: …))  # the ONE two-arg case; returns neg/0/pos
```

- If the function already exists, pass it bare: `key=len`, `key=str.lower`, `key=abs`.
- `key=` takes exactly one argument.
- Late binding: `[lambda: i for i in range(3)]` all return 2. Fix with `lambda i=i: i`.
- lambda is **not** an iteration tool — that's a comprehension.
- Sorts are **stable**: for mixed directions you can't negate, do two passes, least
  significant key first.

---

## 6. Patterns landed 21–22 Sep

```python
# Two Sum — one pass, dict of value -> index. CHECK before you store.
seen = {}
for i, n in enumerate(nums):
    if target - n in seen: return [seen[target - n], i]
    seen[n] = i

# Contains Duplicate — streaming set short-circuits; the one-liner always pays a full pass
for n in nums:
    if n in seen: return True
    seen.add(n)
return len(set(nums)) != len(nums)        # the other answer, for the follow-up

# Group Anagrams — sorted letters as the key
d = defaultdict(list)
for w in strs: d[''.join(sorted(w))].append(w)
return list(d.values())                    # O(n·k log k); count-tuple key makes it O(n·k)

# Longest substring without repeats — window as a set + left pointer.
# Each index enters and leaves once, so the inner while is amortised O(1): truly O(n).
left = 0; seen = set(); best = 0
for right, c in enumerate(s):
    while c in seen:
        seen.remove(s[left]); left += 1
    seen.add(c)
    best = max(best, right - left + 1)

# Subarray Sum Equals K — Two Sum on running sums.
# sum(i..j) = prefix[j] - prefix[i-1] = k  ->  prefix[i-1] = prefix[j] - k
seen = defaultdict(int); seen[0] = 1       # empty prefix: lets a subarray at index 0 count
total = count = 0
for n in nums:
    total += n
    count += seen[total - k]               # count BEFORE inserting, as in Two Sum
    seen[total] += 1
```

**Two pointers require monotonicity.** Negative values break it — extending the window can
lower the sum. Negatives in a subarray-sum problem ⇒ prefix sums + hash map, not a window.

---

## 7. Process rules that cost time when skipped

1. Price every call inside every loop, out loud, before running.
2. Trace one concrete example by hand before coding — control flow you haven't traced is
   where the debugging minutes go.
3. Name variables before typing; never rename mid-solve.
4. Brute force on screen by minute 10, stated *with* its complexity.
5. When something obviously correct fails, read your own identifiers before suspecting Python.
6. Every value the body touches must have arrived through the signature.
7. Say what you return ("return the indices"), not "return true".
8. Constants are worth nothing until the order is right.
