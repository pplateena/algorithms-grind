"""deque and heapq — typing recall.

Why deque: list.pop(0) is O(n) and will time out a BFS on a large grid.
Why heapq: it is a MIN-heap only, and reaching for sort-and-slice instead is
the reflex this file exists to break.

Run:  python3 deques_heaps.py
"""
from drill import run

NUMS = [4, 1, 7, 3, 7, 9, 2]
WORDS = ['pear', 'apple', 'pear', 'fig', 'apple', 'pear']
ADJ = {0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}
PTS = [(1, 2), (3, 1), (-2, 0)]


class Deq:
    """Both ends are O(1). Return lists so the checks can compare."""

    @staticmethod
    def build(nums):
        """A deque from a list, returned as a list.   -> [4, 1, 7, 3, 7, 9, 2]"""
        raise NotImplementedError

    @staticmethod
    def pop_left(nums):
        """Take from the left, return the value.   -> 4"""
        raise NotImplementedError

    @staticmethod
    def push_both_ends(nums, left, right):
        """Add left on the left and right on the right, return as a list.
        ([1,2], 0, 3) -> [0, 1, 2, 3]"""
        raise NotImplementedError

    @staticmethod
    def bfs_order(adj, start):
        """Standard BFS with a deque and a visited set: the order nodes are dequeued.
        (ADJ, 0) -> [0, 1, 2, 3]

        This is the template you will reuse for grids and trees. Write it from memory."""
        raise NotImplementedError


class Heap:
    """heapq works on a plain list, in place. Root is always the smallest."""

    @staticmethod
    def heapify_root(nums):
        """Heapify the list, then return its smallest element.   -> 1"""
        raise NotImplementedError

    @staticmethod
    def push_then_pop(nums, x):
        """Heapify, push x, pop the smallest and return it.   (NUMS, 0) -> 0"""
        raise NotImplementedError

    @staticmethod
    def k_smallest(nums, k):
        """(NUMS, 3) -> [1, 2, 3]   — the module has a one-call answer"""
        raise NotImplementedError

    @staticmethod
    def k_largest(nums, k):
        """(NUMS, 3) -> [9, 7, 7]"""
        raise NotImplementedError

    @staticmethod
    def max_heap_pop(nums):
        """Largest element, using a MIN-heap and the standard trick.   -> 9"""
        raise NotImplementedError


class TopK:
    """The shape Amazon actually asks. No sort-and-slice."""

    @staticmethod
    def top_k_frequent(items, k):
        """The k commonest values, commonest first.   (WORDS, 2) -> ['pear', 'apple']"""
        raise NotImplementedError

    @staticmethod
    def k_closest(pts, k):
        """The k points nearest the origin, no sqrt, via a heap with a key.
        (PTS, 2) -> [(-2, 0), (1, 2)]"""
        raise NotImplementedError


CHECKS = [
    ("deque from list",     lambda: Deq.build(list(NUMS)), [4, 1, 7, 3, 7, 9, 2]),
    ("pop from the left",   lambda: Deq.pop_left(list(NUMS)), 4),
    ("push both ends",      lambda: Deq.push_both_ends([1, 2], 0, 3), [0, 1, 2, 3]),
    ("bfs order",           lambda: Deq.bfs_order(dict(ADJ), 0), [0, 1, 2, 3]),

    ("heapify, root",       lambda: Heap.heapify_root(list(NUMS)), 1),
    ("push 0 then pop",     lambda: Heap.push_then_pop(list(NUMS), 0), 0),
    ("3 smallest",          lambda: Heap.k_smallest(list(NUMS), 3), [1, 2, 3]),
    ("3 largest",           lambda: Heap.k_largest(list(NUMS), 3), [9, 7, 7]),
    ("max via min-heap",    lambda: Heap.max_heap_pop(list(NUMS)), 9),

    ("top 2 frequent",      lambda: TopK.top_k_frequent(list(WORDS), 2), ['pear', 'apple']),
    ("2 closest to origin", lambda: TopK.k_closest(list(PTS), 2), [(-2, 0), (1, 2)]),
]

if __name__ == "__main__":
    run(CHECKS, "deques_heaps.py")
