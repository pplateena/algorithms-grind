"""Numbers and loop skeletons — typing recall.

Run:  python3 numbers.py
"""
from drill import run

NUMS = [4, 1, 7, 3, 7, 9, 2]


class Limits:
    """Sentinels for min/max tracking."""

    @staticmethod
    def positive_infinity():
        """-> inf"""
        raise NotImplementedError

    @staticmethod
    def negative_infinity():
        """-> -inf"""
        raise NotImplementedError


class Math:
    """Integer arithmetic."""

    @staticmethod
    def divmod_pair(a, b):
        """Quotient and remainder in ONE call.   (17, 5) -> (3, 2)"""
        raise NotImplementedError

    @staticmethod
    def floor_div(a, b):
        """Integer division only.   (17, 5) -> 3"""
        raise NotImplementedError

    @staticmethod
    def mid(lo, hi):
        """The midpoint index, integer.   (0, 5) -> 2"""
        raise NotImplementedError

    @staticmethod
    def rounded(x, places):
        """(3.14159, 2) -> 3.14"""
        raise NotImplementedError


class Skeletons:
    """The loop shapes, from memory. These are the ones you re-derive under pressure."""

    @staticmethod
    def two_pointer_reverse(nums):
        """Reverse the list IN PLACE with two pointers — no slicing, no reverse().
        Return it.   -> [2, 9, 7, 3, 7, 1, 4]"""
        raise NotImplementedError

    @staticmethod
    def backwards_indices(nums):
        """Indices from last to first, as a list.   -> [6, 5, 4, 3, 2, 1, 0]"""
        raise NotImplementedError

    @staticmethod
    def pairwise_diffs(nums):
        """Difference between each adjacent pair.   -> [-3, 6, -4, 4, 2, -7]"""
        raise NotImplementedError

    @staticmethod
    def is_sorted(nums):
        """Non-decreasing? One line, using the pairwise idiom.   (NUMS) -> False"""
        raise NotImplementedError

    @staticmethod
    def running_max(nums):
        """Max so far at each position.   -> [4, 4, 7, 7, 7, 9, 9]"""
        raise NotImplementedError


class Convert:
    """Between types."""

    @staticmethod
    def to_int(s):
        """('42') -> 42"""
        raise NotImplementedError

    @staticmethod
    def to_str(n):
        """(42) -> '42'"""
        raise NotImplementedError

    @staticmethod
    def digits(n):
        """The digits of a number as ints.   (407) -> [4, 0, 7]"""
        raise NotImplementedError


CHECKS = [
    ("+inf",                lambda: Limits.positive_infinity(), float('inf')),
    ("-inf",                lambda: Limits.negative_infinity(), float('-inf')),

    ("divmod 17, 5",        lambda: Math.divmod_pair(17, 5), (3, 2)),
    ("floor div",           lambda: Math.floor_div(17, 5), 3),
    ("midpoint of 0, 5",    lambda: Math.mid(0, 5), 2),
    ("round to 2",          lambda: Math.rounded(3.14159, 2), 3.14),

    ("two-pointer reverse", lambda: Skeletons.two_pointer_reverse(list(NUMS)), [2, 9, 7, 3, 7, 1, 4]),
    ("backwards indices",   lambda: Skeletons.backwards_indices(list(NUMS)), [6, 5, 4, 3, 2, 1, 0]),
    ("pairwise diffs",      lambda: Skeletons.pairwise_diffs(list(NUMS)), [-3, 6, -4, 4, 2, -7]),
    ("is sorted",           lambda: Skeletons.is_sorted(list(NUMS)), False),
    ("running max",         lambda: Skeletons.running_max(list(NUMS)), [4, 4, 7, 7, 7, 9, 9]),

    ("to int",              lambda: Convert.to_int('42'), 42),
    ("to str",              lambda: Convert.to_str(42), '42'),
    ("digits of 407",       lambda: Convert.digits(407), [4, 0, 7]),
]

if __name__ == "__main__":
    run(CHECKS, "numbers.py")
