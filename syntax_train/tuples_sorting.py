"""Tuples and multi-key sorting — typing recall.

Run:  python3 tuples_sorting.py
"""
from drill import run

PEOPLE = [('ann', 30), ('bob', 25), ('cid', 30)]
WORDS = ['bb', 'a', 'ccc', 'dd']
NUMS = [4, 1, 7, 3, 7, 9, 2]


class Unpack:
    """The right-hand side is fully evaluated before any target is assigned."""

    @staticmethod
    def two_names(pair):
        """Unpack a 2-tuple and return them swapped.   (('x', 9)) -> (9, 'x')"""
        raise NotImplementedError

    @staticmethod
    def first_and_rest(nums):
        """(first, [everything else]).   -> (4, [1, 7, 3, 7, 9, 2])"""
        raise NotImplementedError

    @staticmethod
    def init_and_last(nums):
        """([everything but the last], last).   -> ([4, 1, 7, 3, 7, 9], 2)"""
        raise NotImplementedError

    @staticmethod
    def swap_indices(nums, i, j):
        """Swap two positions in place with no temp variable, return the list.
        (NUMS, 0, 6) -> [2, 1, 7, 3, 7, 9, 4]"""
        raise NotImplementedError


class MultiKey:
    """A tuple key sorts by its first element, then the second, and so on."""

    @staticmethod
    def by_age(people):
        """Ascending age.   -> [('bob',25), ('ann',30), ('cid',30)]"""
        raise NotImplementedError

    @staticmethod
    def by_age_desc_then_name(people):
        """Age descending, then name ascending. One key, one negation.
        -> [('ann',30), ('cid',30), ('bob',25)]"""
        raise NotImplementedError

    @staticmethod
    def by_length_then_alpha(words):
        """-> ['a', 'bb', 'dd', 'ccc']"""
        raise NotImplementedError


class Stability:
    """Python's sort is stable: equal keys keep their previous relative order."""

    @staticmethod
    def two_pass(words):
        """Length DESCENDING, then alphabetical ASCENDING — using two stable passes
        instead of one tuple key. Least significant key first.
        -> ['ccc', 'bb', 'dd', 'a']"""
        raise NotImplementedError


CHECKS = [
    ("unpack and swap",        lambda: Unpack.two_names(('x', 9)), (9, 'x')),
    ("first and rest",         lambda: Unpack.first_and_rest(list(NUMS)), (4, [1, 7, 3, 7, 9, 2])),
    ("init and last",          lambda: Unpack.init_and_last(list(NUMS)), ([4, 1, 7, 3, 7, 9], 2)),
    ("swap indices 0 and 6",   lambda: Unpack.swap_indices(list(NUMS), 0, 6), [2, 1, 7, 3, 7, 9, 4]),

    ("by age",                 lambda: MultiKey.by_age(list(PEOPLE)), [('bob', 25), ('ann', 30), ('cid', 30)]),
    ("age desc then name",     lambda: MultiKey.by_age_desc_then_name(list(PEOPLE)), [('ann', 30), ('cid', 30), ('bob', 25)]),
    ("length then alpha",      lambda: MultiKey.by_length_then_alpha(list(WORDS)), ['a', 'bb', 'dd', 'ccc']),

    ("two stable passes",      lambda: Stability.two_pass(list(WORDS)), ['ccc', 'bb', 'dd', 'a']),
]

if __name__ == "__main__":
    run(CHECKS, "tuples_sorting.py")
