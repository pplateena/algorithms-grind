# syntax_train

Typing recall for the Python standard library. No algorithms — the point is that
`heapq.heappush` and `d.get(k, 0)` arrive without a lookup, so the 25 minutes in a
round go to the problem instead of the API.

## How to use

One file per data type. Inside a file, one class per group of related operations,
one method per line of syntax you have to produce. Fill the method body; type your
answer **above** the `raise NotImplementedError` so you never have to delete it.

```bash
python3 lists.py        # .. pending / ok / FAIL per check, plus a count
```

Rules:

1. Write from memory. If it doesn't come in ~20 seconds, look it up, close the tab,
   then type it from memory.
2. Everything you looked up goes into `syntax.md` in your own words before you move on.
   That file, not these, is the cheat sheet.
3. Run the file. A check you never ran is a check you don't know.

Inputs are module-level constants. Every check passes a **fresh copy**, so a method
that mutates can't corrupt the ones after it.

## Files

| File | Covers |
|---|---|
| `lists.py` | search, order, slice, transform, mutate, build |
| `strings.py` | split/join, chars, find, compare |
| `dicts.py` | access, order, transform, counting, iterate |
| `sets.py` | build, the operator forms, membership, dedupe |
| `tuples_sorting.py` | unpacking, multi-key sorts, stability |
| `lambdas.py` | `key=`, passing a function bare, factories, `cmp_to_key`, late binding |
| `deques_heaps.py` | `deque` ends, BFS skeleton, `heapq`, top-k |
| `search.py` | `bisect`, hand-rolled binary search |
| `grids.py` | shape, non-aliased construction, neighbours, transpose/rotate |
| `numbers.py` | infinities, `divmod`, countdowns, two-pointer skeleton |

`day1-syntax.py` is the older single-file version (lists + lambda filled in, 22 Sep).
Kept as a re-test.
