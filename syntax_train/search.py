"""bisect and hand-rolled binary search — typing recall.

bisect finds the position in O(log n); insort then INSERTS in O(n), because
everything shifts. If your instinct is "keep a sorted list and insert into it",
that is usually the signal to reach for a heap.

Run:  python3 search.py
"""
from drill import run

ARR = [1, 3, 3, 5, 7, 9]


class Bisect:
    """Insertion points into an already-sorted list."""

    @staticmethod
    def left_index(arr, x):
        """Leftmost position where x could go.   (ARR, 3) -> 1"""
        raise NotImplementedError

    @staticmethod
    def right_index(arr, x):
        """Rightmost such position.   (ARR, 3) -> 3"""
        raise NotImplementedError

    @staticmethod
    def first_ge(arr, x):
        """Index of the first element >= x.   (ARR, 6) -> 4"""
        raise NotImplementedError

    @staticmethod
    def insert_sorted(arr, x):
        """Insert keeping order, return the list.   (ARR, 4) -> [1,3,3,4,5,7,9]"""
        raise NotImplementedError


class Hand:
    """Write these from memory — an interviewer will ask you to, and bisect is banned."""

    @staticmethod
    def binary_search(arr, target):
        """Index of target, or -1. lo/hi/mid, no bisect.   (ARR, 7) -> 4"""
        raise NotImplementedError

    @staticmethod
    def first_true(arr, threshold):
        """Index of the first element > threshold, or len(arr) if none.
        Binary search on a predicate — the shape behind "binary search the answer".
        (ARR, 4) -> 3"""
        raise NotImplementedError


CHECKS = [
    ("bisect_left 3",     lambda: Bisect.left_index(list(ARR), 3), 1),
    ("bisect_right 3",    lambda: Bisect.right_index(list(ARR), 3), 3),
    ("first >= 6",        lambda: Bisect.first_ge(list(ARR), 6), 4),
    ("insort 4",          lambda: Bisect.insert_sorted(list(ARR), 4), [1, 3, 3, 4, 5, 7, 9]),

    ("binary search 7",   lambda: Hand.binary_search(list(ARR), 7), 4),
    ("first > 4",         lambda: Hand.first_true(list(ARR), 4), 3),
]

if __name__ == "__main__":
    run(CHECKS, "search.py")
