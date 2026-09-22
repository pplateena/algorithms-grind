"""Sets — typing recall.

Cost note, because this one bit you: MEMBERSHIP (`x in s`) is O(1).
Comparing or intersecting two sets is O(n) in the smaller one. Not the same thing.

Run:  python3 sets.py
"""
from drill import run

A, B = {1, 2, 3, 4}, {3, 4, 5}
NUMS = [4, 1, 7, 3, 7, 9, 2]


class Build:
    """Making sets. The empty one has no literal — that is the whole trap."""

    @staticmethod
    def empty():
        """An empty set. `{}` is a dict.   -> set()"""
        raise NotImplementedError

    @staticmethod
    def literal():
        """A set holding 1 and 2, written as a literal.   -> {1, 2}"""
        raise NotImplementedError

    @staticmethod
    def from_list(nums):
        """Unique values.   -> {1, 2, 3, 4, 7, 9}"""
        raise NotImplementedError

    @staticmethod
    def add_then_discard(x, y):
        """Start empty, add x, then remove y WITHOUT raising if it is absent.
        Return the set.   (1, 99) -> {1}"""
        raise NotImplementedError

    @staticmethod
    def visited_cells():
        """A set holding the coordinates (0,0) and (1,2) — think about hashability.
        -> {(0, 0), (1, 2)}"""
        raise NotImplementedError


class Ops:
    """The operator forms read faster under pressure than the method names."""

    @staticmethod
    def union(a, b):
        """-> {1, 2, 3, 4, 5}"""
        raise NotImplementedError

    @staticmethod
    def intersection(a, b):
        """-> {3, 4}"""
        raise NotImplementedError

    @staticmethod
    def difference(a, b):
        """In a but not b.   -> {1, 2}"""
        raise NotImplementedError

    @staticmethod
    def symmetric_difference(a, b):
        """In exactly one of the two.   -> {1, 2, 5}"""
        raise NotImplementedError

    @staticmethod
    def is_superset(a, other):
        """Does a contain all of other.   (A, {1,2}) -> True"""
        raise NotImplementedError

    @staticmethod
    def is_disjoint(a, other):
        """No overlap at all.   (A, {9}) -> True"""
        raise NotImplementedError


class Use:
    """What sets are actually for in a round."""

    @staticmethod
    def has_duplicate(nums):
        """True if any value repeats — the one-line version.   -> True"""
        raise NotImplementedError

    @staticmethod
    def first_repeat(nums):
        """The first value seen twice, scanning left to right; None if all distinct.
        Short-circuits, unlike the one-liner above.   -> 7"""
        raise NotImplementedError

    @staticmethod
    def dedupe_keep_order(nums):
        """Unique values in first-seen order — a set alone loses the order.
        -> [4, 1, 7, 3, 9, 2]"""
        raise NotImplementedError


CHECKS = [
    ("empty set",            lambda: Build.empty(), set()),
    ("set literal",          lambda: Build.literal(), {1, 2}),
    ("from list",            lambda: Build.from_list(list(NUMS)), {1, 2, 3, 4, 7, 9}),
    ("add then discard",     lambda: Build.add_then_discard(1, 99), {1}),
    ("visited cells",        lambda: Build.visited_cells(), {(0, 0), (1, 2)}),

    ("union",                lambda: Ops.union(set(A), set(B)), {1, 2, 3, 4, 5}),
    ("intersection",         lambda: Ops.intersection(set(A), set(B)), {3, 4}),
    ("difference",           lambda: Ops.difference(set(A), set(B)), {1, 2}),
    ("symmetric difference", lambda: Ops.symmetric_difference(set(A), set(B)), {1, 2, 5}),
    ("is superset",          lambda: Ops.is_superset(set(A), {1, 2}), True),
    ("is disjoint",          lambda: Ops.is_disjoint(set(A), {9}), True),

    ("has duplicate",        lambda: Use.has_duplicate(list(NUMS)), True),
    ("first repeat",         lambda: Use.first_repeat(list(NUMS)), 7),
    ("dedupe keep order",    lambda: Use.dedupe_keep_order(list(NUMS)), [4, 1, 7, 3, 9, 2]),
]

if __name__ == "__main__":
    run(CHECKS, "sets.py")
