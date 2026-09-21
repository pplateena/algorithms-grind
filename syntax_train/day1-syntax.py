# %% [markdown]
# # Day 1 syntax drill
#
# Typing recall only. No algorithms here.
#
# **How to use.** Write each line from memory. If it does not come in ~20 seconds, look it
# up, close the tab, then type it again from memory. Print every answer and check it against
# the `->` value in the comment.
#
# `CORE` marks the ~65 lines worth doing first; budget 40 minutes for those. The rest is
# overflow for Days 2-4 warm-ups.
#
# Anything you had to look up goes into `syntax.md` in your own words before you move on.
# That file, not this one, is your Day 4 cheat sheet.

# %% [markdown]
# ## 0. Imports
#
# Written from memory every time. Forgetting these mid-problem costs a lookup.

# %%
# CORE  the five imports you need in almost every problem:
#       deque, Counter, defaultdict, heapq, bisect

from collections import defaultdict, deque # don't know from where heapq, counter and bisect are imported
# CORE  raise the recursion limit (deep trees blow the default ~1000)

# %% [markdown]
# ## 1. Lists
#
# Anything that mutates: work on nums.copy() so later tasks still see the original.

# %%
nums = [4, 1, 7, 3, 7, 9, 2]
nested = [[1, 2], [3], [4, 5]]
a, b = [1, 2, 3], ['x', 'y', 'z']

# CORE  index of the first 7 in nums                         -> 3
# idx = nums.index(7) # don't know if correct method call here
print('index of the first 7 in nums', nums.index(7))
print(nums.index(7)+1 == 3)
# how many 7s in nums                                        -> 2
# amount = count(7, nums) # don't know if correct method call here
amount = nums.count(7)
print(amount == 2)
# CORE  a new sorted list, ascending                         -> [1, 2, 3, 4, 7, 7, 9]

# nums.sort() # i think this is in place
sort_asc = sorted(nums) # i think this isnt in place
# don't know if reverse=false have to passed
# don't know whether this
print(sorted(nums) == [1, 2, 3, 4, 7, 7, 9])

# CORE  sort a copy in place, descending                     -> [9, 7, 7, 4, 3, 2, 1]
nums_copy = nums.copy()
nums_copy.sort(reverse = True)
print('CORE  sort a copy in place, descending', nums_copy)
print(nums_copy == [9, 7, 7, 4, 3, 2, 1])
# don't remeber whether reverse is decalred correctly, or

# last element                                               -> 2
nums_copy = nums.copy()
last = nums_copy.pop()
print(last == 2)
# last three elements                                        -> [7, 9, 2]
last_three = nums[-3:]
print('last three elements', last_three)
print(last_three == [7, 9, 2])
# every second element                                       -> [4, 7, 7, 2]
every_second = nums[::2]
print(every_second == [4, 7, 7, 2])
# CORE  a reversed copy                                      -> [2, 9, 7, 3, 7, 1, 4]
nums_copy = nums.copy()
reverse = nums_copy[::-1]
print('CORE  a reversed copy', reverse)
print(reverse == [2, 9, 7, 3, 7, 1, 4])
# CORE  squares of the odd values                            -> [1, 49, 9, 49, 81]

new = [] # brute force
for idx, value in enumerate(nums): # dont' remember whether this is correct declaration
        if value % 2:
                new.append(value*value)
print('squares of the odd values', new )
print(new == [1, 49, 9, 49, 81])

# nums = [n*n if nums.index(n) % 2 else n for n in nums] # list comprehension, not sure if this would work

# i think this can be done via lambda as well, don't remember syntax for it

# as well this is probably doable via slicng [::2], mine try:
# doesnt work new = nums[::*2] # wouldn't work, don't remember how to do it

# sum of nums                                                -> 33
sum(nums)
s = 0
for n in nums:
        s += n
print(sum(nums) == 33, s == 33)

# CORE  the max value and its index                          -> 9, 5
m = max(nums) # not sure whether index can be returned at this step
m_idx = nums.index(m) # not sure whether correct index
print((m, m_idx) == (9,5))
# CORE  flatten nested                                       -> [1, 2, 3, 4, 5]
flat = []
for n in nested:
        flat += n
print(flat == [1, 2, 3, 4, 5])
# pretty sure can be done via zip unzip, don't know how.
# can't remember how to write list comprehension here

# CORE  (index, value) pairs where value > 5                 -> [(2, 7), (4, 7), (5, 9)]
pairs = []
for idx, value in enumerate(nums):
        if value > 5:
                pairs.append((idx,value))
print(pairs == [(2, 7), (4, 7), (5, 9)])
# maybe doable via lambda

# CORE  pair up a and b                                      -> [(1, 'x'), (2, 'y'), (3, 'z')]
# maybe doable via zip and lambda
# risky if diff sizes

if len(a) == len(b):
        new = []
        for idx, val in enumerate(a):
                new.append((val, b[idx]))
else:
        print("Size invariant can be done via while, don't want to waste time")

print(new == [(1, 'x'), (2, 'y'), (3, 'z')])
# swap first and last of a copy                              -> [2, 1, 7, 3, 7, 9, 4]

# dont remember copies, not sure how to do this correctly, different methods doable here

# bad solution new = [nums.pop()] + nums[1:] + [nums.pop(0)] # not sure whether this would work

# new = nums.copy()[1:-1]
# first, last = nums.pop(0), nums.pop()
# new = [first] + new + last

new = nums[-1:] + nums[1:-1] + nums[:1]
print('swap first and last of a copy', nums, new)
print(new == [2, 1, 7, 3, 7, 9, 4])

# CORE  a list of five zeros                                 -> [0, 0, 0, 0, 0]
zeros = [0] * 5
print(zeros == [0, 0, 0, 0, 0])
# insert 99 at index 2 of a copy                             -> [4, 1, 99, 7, 3, 7, 9, 2]
# dont know about copies here, and don't know correct insertion syntax
inserted = nums.copy()
inserted.insert(2, 99)
print(inserted == [4, 1, 99, 7, 3, 7, 9, 2])
# remove the first 7 from a copy                             -> [4, 1, 3, 7, 9, 2]
# i don't remember how to use remove correcly, brute force would be to iterate,
# but i am pretty sure it can be done via something like .remove() | .delete(7, reverse=False, amount = 1)

for idx, n in enumerate(nums):
        if n == 7:
                rem_idx = idx
                break



rem = nums.copy()
rem.pop(rem_idx) # i think idx parameter would work as well, .pop() returns value, and modifies list - i probably made mistakes with this earlier
print(rem == [4, 1, 3, 7, 9, 2])
# pop the last element off a copy and keep the value         -> 2

# %% [markdown]
# ## 2. Strings

# %%
s = "the quick brown fox jumps"
t, u = "Listen", "silent"

# CORE  split s into words                     -> ['the', 'quick', 'brown', 'fox', 'jumps']

# CORE  join those words with '-'              -> 'the-quick-brown-fox-jumps'

# CORE  reverse s                              -> 'spmuj xof nworb kciuq eht'

# CORE  are t and u anagrams (case-insensitive, via sorted)   -> True

# CORE  same check, via Counter                               -> True

# how many 'o' in s                            -> 2

# CORE  alphabet position of 'c' (a=0)         -> 2

# CORE  the letter at alphabet position 25     -> 'z'

# index where 'brown' starts                   -> 10

# index of 'cat', without raising              -> -1

# does s end with 'jumps'                      -> True

# f-string: "fox appears at 16"  (compute the 16)

# are all characters of s alphanumeric         -> False

# s with spaces stripped out                   -> 'thequickbrownfoxjumps'

# %% [markdown]
# ## 3. Dicts

# %%
d = {'a': 3, 'b': 1, 'c': 2}
words = ['pear', 'apple', 'pear', 'fig', 'apple', 'pear']

# CORE  value of 'z', defaulting to 0                -> 0

# CORE  increment the count of 'z' safely (no KeyError)

# CORE  items sorted by value, descending            -> [('a', 3), ('c', 2), ('b', 1)]

# CORE  the key with the largest value               -> 'a'

# CORE  {k: v * 2 for ...}                           -> {'a': 6, 'b': 2, 'c': 4}

# is 'b' a key                                       -> True

# delete 'b' from a copy; pop 'z' with a default     -> 0

# CORE  frequency table of words                     -> Counter({'pear': 3, 'apple': 2, 'fig': 1})

# CORE  the single most common word and its count    -> [('pear', 3)]

# CORE  group words by first letter, defaultdict(list)
#       -> {'p': ['pear', 'pear', 'pear'], 'a': ['apple', 'apple'], 'f': ['fig']}

# invert d                                           -> {3: 'a', 1: 'b', 2: 'c'}

# iterate key and value together in one loop

# %% [markdown]
# ## 4. Sets
#
# The operator forms matter: | & - ^ read faster than the method names under pressure.

# %%
A, B = {1, 2, 3, 4}, {3, 4, 5}
nums = [4, 1, 7, 3, 7, 9, 2]

# CORE  union                       -> {1, 2, 3, 4, 5}

# CORE  intersection                -> {3, 4}

# CORE  in A but not in B           -> {1, 2}

# CORE  in exactly one of the two   -> {1, 2, 5}

# CORE  is 3 in A                   -> True

# add 9 to a copy of A; remove 1 without raising if absent

# does A contain all of {1, 2}      -> True

# CORE  dedupe nums, preserving order  -> [4, 1, 7, 3, 9, 2]

# CORE  dedupe nums, order irrelevant  -> {1, 2, 3, 4, 7, 9}

# set of the squares of A           -> {1, 4, 9, 16}

# an empty set (not an empty dict)

# %% [markdown]
# ## 5. Tuples & multi-key sorting

# %%
people = [('ann', 30), ('bob', 25), ('cid', 30)]

# CORE  unpack ('x', 9) into two names

# CORE  sort by age ascending    -> [('bob', 25), ('ann', 30), ('cid', 30)]

# CORE  sort by age descending, then name ascending
#                                -> [('ann', 30), ('cid', 30), ('bob', 25)]

# the entry with the smallest age   -> ('bob', 25)

# CORE  a set holding the visited cells (0, 0) and (1, 2)

# sort ['pear', 'fig', 'apple'] by length, then alphabetically -> ['fig', 'pear', 'apple']

# %% [markdown]
# ## 5b. lambda
#
# `lambda` is an expression whose value is a function. Body = ONE expression: no assignment,
# no loops, no `return` (the expression is the return value). A ternary is allowed.
# Never name one — its only job is to be passed inline, almost always to `key=`.
#
# Model for `key=`: given ONE element, what value should be compared in its place?
# Python calls it once per element and hands back the ORIGINAL elements, sorted by the result.

# %%
pairs = [('pear', 3), ('apple', 2), ('fig', 5)]
words = ['bb', 'a', 'ccc', 'dd']
pts = [(1, 2), (3, 1), (-2, 0)]

# CORE  sort pairs by count, descending          -> [('fig', 5), ('pear', 3), ('apple', 2)]

# CORE  sort words by length, then alphabetically   -> ['a', 'bb', 'dd', 'ccc']

# CORE  the pair with the largest count          -> ('fig', 5)
#       (returns the PAIR, not the count)

# CORE  sort pts by distance from the origin, no sqrt   -> [(-2, 0), (1, 2), (3, 1)]

# CORE  a defaultdict whose missing value is -1

# CORE  sort words by length DESCENDING, then alphabetically ascending  -> ['ccc', 'bb', 'dd', 'a']
#       (length negates, the string cannot — this is the real test)

# sort words by length, with NO lambda            -> ['a', 'bb', 'dd', 'ccc']
#       (when the function already exists, pass it bare)

# sort ['Fig', 'apple', 'Pear'] case-insensitively, no lambda  -> ['apple', 'Fig', 'Pear']

# sort [3, -7, 2] by magnitude, no lambda         -> [2, 3, -7]

# a two-argument comparison sort of [3, 1, 2], ascending, via functools
#       (the only place a sorting lambda takes TWO args; returns neg / 0 / pos)

# why does [lambda: i for i in range(3)] give three functions that all return 2,
# and what one-token change fixes it?

# %% [markdown]
# ## 6. deque
#
# list.pop(0) is O(n) and will time out a BFS on a large grid. This is why.

# %%
# CORE  a deque from [1, 2, 3]

# CORE  take from the left            -> 1

# CORE  add 0 on the left, 4 on the right

# take from the right                 -> 4

# CORE  the BFS skeleton, from memory: queue holding a start node,
#       loop while it is non-empty, pop from the left each round


# a deque that keeps only its last 3 items

# %% [markdown]
# ## 7. heapq
#
# Your named gap: reaching for sort-and-slice where a heap is the answer. Do all of these with heapq.

# %%
costs = [5, 1, 8, 3, 9, 2]

# CORE  turn a copy of costs into a heap in place

# CORE  push 4, then pop the smallest        -> 1

# CORE  the 3 smallest                       -> [1, 2, 3]

# CORE  the 3 largest                        -> [9, 8, 5]

# CORE  the largest, using a min-heap and negation   -> 9

# CORE  2nd largest via a min-heap of size k=2, no full sort   -> 8

# CORE  push the pairs (5, 'a') and (2, 'b'), pop the smallest -> (2, 'b')

# push 7 and pop the smallest in one operation

# why (cost, node) and not (node, cost)?  answer in a comment:

# %% [markdown]
# ## 8. bisect & binary search

# %%
arr = [1, 3, 3, 5, 7, 9]

# CORE  leftmost insertion point for 3      -> 1

# rightmost insertion point for 3           -> 3

# CORE  index of the first element >= 6     -> 4

# insert 4 into a copy, keeping it sorted   -> [1, 3, 3, 4, 5, 7, 9]

# CORE  hand-written binary search for 7, returning its index -> 4
#       (lo/hi/mid, from memory, no bisect)

# %% [markdown]
# ## 9. 2D grids
#
# [[0]*n]*m gives you m references to ONE row. It is the single most common silent bug here.

# %%
grid = [[1, 1, 0],
        [0, 1, 0],
        [0, 0, 1]]

# CORE  number of rows and columns             -> 3, 3

# CORE  a 3x4 grid of zeros, rows not aliased  -> [[0,0,0,0], [0,0,0,0], [0,0,0,0]]

# CORE  the four direction deltas as a list of pairs

# CORE  an is-inside-the-grid check for (r, c), as a one-liner

# how many 1s in grid                          -> 4

# CORE  loop over every cell with its (r, c) indices

# transpose grid    -> [[1, 0, 0], [1, 1, 0], [0, 0, 1]]

# an independent copy of grid (mutating the copy must not touch grid)

# CORE  the four neighbours of (1, 1) that are inside the grid -> [(0,1), (2,1), (1,0), (1,2)]

# %% [markdown]
# ## 10. Numbers & control flow

# %%
# CORE  positive and negative infinity

# CORE  quotient and remainder of 17 by 5 in one call   -> (3, 2)

# integer division and remainder separately             -> 3, 2

# CORE  count down 5, 4, 3, 2, 1

# CORE  is any value in [4, 1, 7] greater than 6        -> True

# CORE  are all values in [4, 1, 7] positive            -> True

# CORE  two-pointer skeleton over a list: left at the start,
#       right at the end, loop while they have not met


# int from '42', str from 42

# round 3.14159 to 2 places, and the absolute value of -5

# %% [markdown]
# ## 11. Day 2 preview (optional)
#
# Only if the first ten cells went fast.

# %%
edges = [(0, 1), (0, 2), (1, 3)]

# a binary tree node class: value, left, right


# CORE  adjacency list from edges, undirected
#       -> {0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}

# recursive DFS over a tree, returning its depth


# iterative BFS over a graph with a visited set
