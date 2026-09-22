"""Lists — typing recall.

Fill each body. Type your answer ABOVE the `raise NotImplementedError`.
Run:  python3 lists.py
"""
from drill import run

NUMS = [4, 1, 7, 3, 7, 9, 2]
NESTED = [[1, 2], [3], [4, 5]]
A = [1, 2, 3]
B = ['x', 'y', 'z']


class Search:
    """Locate values in a list. Takes a list, returns an index / count / bool. Never mutates.

    Cost note: every method here is O(n). That is the point — none of them is free.
    """

    @staticmethod
    def first_index(nums, x):
        """Index of the first x.   ([4,1,7,3,7], 7) -> 2"""
        raise NotImplementedError

    @staticmethod
    def count_of(nums, x):
        """How many x.   ([4,1,7,3,7], 7) -> 2"""
        raise NotImplementedError

    @staticmethod
    def max_value(nums):
        """Largest value.   -> 9"""
        raise NotImplementedError

    @staticmethod
    def index_of_max(nums):
        """Index of the largest value.   -> 5"""
        raise NotImplementedError

    @staticmethod
    def contains(nums, x):
        """Is x present. O(n) — the reason a set exists.   -> True"""
        raise NotImplementedError

    @staticmethod
    def any_over(nums, limit):
        """Is any value > limit.   (NUMS, 8) -> True"""
        raise NotImplementedError

    @staticmethod
    def all_positive(nums):
        """Are all values > 0.   -> True"""
        raise NotImplementedError


class Order:
    """Sorting and reversing. Returns a NEW list unless the name says in_place."""

    @staticmethod
    def ascending(nums):
        """A new sorted list.   -> [1, 2, 3, 4, 7, 7, 9]"""
        raise NotImplementedError

    @staticmethod
    def descending(nums):
        """A new list, largest first.   -> [9, 7, 7, 4, 3, 2, 1]"""
        raise NotImplementedError

    @staticmethod
    def reversed_copy(nums):
        """Reversed, NOT sorted.   -> [2, 9, 7, 3, 7, 1, 4]"""
        raise NotImplementedError

    @staticmethod
    def sort_in_place_desc(nums):
        """Sort the given list itself, descending, then return it.
        Watch the trap: the sort method returns None.   -> [9, 7, 7, 4, 3, 2, 1]"""
        raise NotImplementedError


class Slice:
    """Position selection. A slice never transforms values, and never raises."""

    @staticmethod
    def last_three(nums):
        """-> [7, 9, 2]"""
        raise NotImplementedError

    @staticmethod
    def every_second(nums):
        """-> [4, 7, 7, 2]"""
        raise NotImplementedError

    @staticmethod
    def middle(nums):
        """Everything except the first and last.   -> [1, 7, 3, 7, 9]"""
        raise NotImplementedError

    @staticmethod
    def past_the_end(nums):
        """Items from index 99 onward. Slicing does not raise.   -> []"""
        raise NotImplementedError


class Transform:
    """Comprehensions: [expr for x in it if cond] — expr maps, if filters."""

    @staticmethod
    def squares_of_odds(nums):
        """Squares of the odd VALUES.   -> [1, 49, 9, 49, 81]"""
        raise NotImplementedError

    @staticmethod
    def indexed_over(nums, limit):
        """(index, value) pairs where value > limit.   (NUMS, 5) -> [(2,7), (4,7), (5,9)]"""
        raise NotImplementedError

    @staticmethod
    def flatten(nested):
        """One level down. Outer loop first.   -> [1, 2, 3, 4, 5]"""
        raise NotImplementedError

    @staticmethod
    def pair_up(a, b):
        """-> [(1, 'x'), (2, 'y'), (3, 'z')]   (stops at the shorter one)"""
        raise NotImplementedError

    @staticmethod
    def total(nums):
        """Sum.   -> 33"""
        raise NotImplementedError


class Mutate:
    """Changes the list it is given, then returns it so the check can see the result.

    Every one of these returns None from the underlying method — that is the trap.
    """

    @staticmethod
    def swap_ends(nums):
        """Swap first and last, return the list.   -> [2, 1, 7, 3, 7, 9, 4]"""
        raise NotImplementedError

    @staticmethod
    def insert_at(nums, i, x):
        """Insert x at index i, return the list.   (NUMS, 2, 99) -> [4,1,99,7,3,7,9,2]"""
        raise NotImplementedError

    @staticmethod
    def remove_first(nums, x):
        """Remove the first x, return the list.   (NUMS, 7) -> [4, 1, 3, 7, 9, 2]"""
        raise NotImplementedError

    @staticmethod
    def pop_last(nums):
        """Return (popped value, the remaining list).   -> (2, [4, 1, 7, 3, 7, 9])"""
        raise NotImplementedError

    @staticmethod
    def replace_contents(nums, other):
        """Replace the contents of nums IN PLACE with other's, return nums.
        The caller must see the change, so rebinding the name is wrong.
        (NUMS, [8, 8]) -> [8, 8]"""
        raise NotImplementedError


class Build:
    """Making lists from nothing."""

    @staticmethod
    def zeros(n):
        """(5) -> [0, 0, 0, 0, 0]"""
        raise NotImplementedError

    @staticmethod
    def from_range(start, stop):
        """(2, 6) -> [2, 3, 4, 5]"""
        raise NotImplementedError

    @staticmethod
    def countdown(n):
        """(5) -> [5, 4, 3, 2, 1]"""
        raise NotImplementedError


CHECKS = [
    ("first index of 7",        lambda: Search.first_index(list(NUMS), 7), 2),
    ("count of 7",              lambda: Search.count_of(list(NUMS), 7), 2),
    ("max value",               lambda: Search.max_value(list(NUMS)), 9),
    ("index of max",            lambda: Search.index_of_max(list(NUMS)), 5),
    ("contains 3",              lambda: Search.contains(list(NUMS), 3), True),
    ("any over 8",              lambda: Search.any_over(list(NUMS), 8), True),
    ("all positive",            lambda: Search.all_positive(list(NUMS)), True),

    ("ascending",               lambda: Order.ascending(list(NUMS)), [1, 2, 3, 4, 7, 7, 9]),
    ("descending",              lambda: Order.descending(list(NUMS)), [9, 7, 7, 4, 3, 2, 1]),
    ("reversed copy",           lambda: Order.reversed_copy(list(NUMS)), [2, 9, 7, 3, 7, 1, 4]),
    ("sort in place desc",      lambda: Order.sort_in_place_desc(list(NUMS)), [9, 7, 7, 4, 3, 2, 1]),

    ("last three",              lambda: Slice.last_three(list(NUMS)), [7, 9, 2]),
    ("every second",            lambda: Slice.every_second(list(NUMS)), [4, 7, 7, 2]),
    ("middle",                  lambda: Slice.middle(list(NUMS)), [1, 7, 3, 7, 9]),
    ("past the end",            lambda: Slice.past_the_end(list(NUMS)), []),

    ("squares of odds",         lambda: Transform.squares_of_odds(list(NUMS)), [1, 49, 9, 49, 81]),
    ("indexed over 5",          lambda: Transform.indexed_over(list(NUMS), 5), [(2, 7), (4, 7), (5, 9)]),
    ("flatten",                 lambda: Transform.flatten([r[:] for r in NESTED]), [1, 2, 3, 4, 5]),
    ("pair up",                 lambda: Transform.pair_up(list(A), list(B)), [(1, 'x'), (2, 'y'), (3, 'z')]),
    ("total",                   lambda: Transform.total(list(NUMS)), 33),

    ("swap ends",               lambda: Mutate.swap_ends(list(NUMS)), [2, 1, 7, 3, 7, 9, 4]),
    ("insert 99 at 2",          lambda: Mutate.insert_at(list(NUMS), 2, 99), [4, 1, 99, 7, 3, 7, 9, 2]),
    ("remove first 7",          lambda: Mutate.remove_first(list(NUMS), 7), [4, 1, 3, 7, 9, 2]),
    ("pop last",                lambda: Mutate.pop_last(list(NUMS)), (2, [4, 1, 7, 3, 7, 9])),
    ("replace contents",        lambda: Mutate.replace_contents(list(NUMS), [8, 8]), [8, 8]),

    ("zeros",                   lambda: Build.zeros(5), [0, 0, 0, 0, 0]),
    ("from range",              lambda: Build.from_range(2, 6), [2, 3, 4, 5]),
    ("countdown",               lambda: Build.countdown(5), [5, 4, 3, 2, 1]),
]

if __name__ == "__main__":
    run(CHECKS, "lists.py")
