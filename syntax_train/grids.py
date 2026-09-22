"""2D grids — typing recall.

[[0]*n]*m gives you m references to ONE row. That is the single most common
silent bug in grid problems: `*` is safe only for immutables.

Run:  python3 grids.py
"""
from drill import run

GRID = [[1, 1, 0],
        [0, 1, 0],
        [0, 0, 1]]


class Shape:
    """Dimensions and counting."""

    @staticmethod
    def dims(grid):
        """(rows, cols).   -> (3, 3)"""
        raise NotImplementedError

    @staticmethod
    def count_value(grid, x):
        """How many cells equal x.   (GRID, 1) -> 4"""
        raise NotImplementedError

    @staticmethod
    def flatten(grid):
        """Row-major.   -> [1, 1, 0, 0, 1, 0, 0, 0, 1]"""
        raise NotImplementedError


class Build:
    """Construction that does not alias."""

    @staticmethod
    def zeros(rows, cols):
        """Independent rows.   (2, 3) -> [[0,0,0], [0,0,0]]"""
        raise NotImplementedError

    @staticmethod
    def deep_copy(grid):
        """A copy whose rows are independent of the original's.   -> same values"""
        raise NotImplementedError

    @staticmethod
    def aliased_proof(rows, cols):
        """Build the WRONG way ([[0]*cols]*rows), set [0][0] = 9, return the grid.
        The expected value shows you what aliasing does.   (2, 3) -> [[9,0,0], [9,0,0]]"""
        raise NotImplementedError


class Move:
    """Neighbours. The two lines every grid BFS needs."""

    @staticmethod
    def directions():
        """The four orthogonal deltas, as a list of (dr, dc) — up, down, left, right
        in any order but return exactly this one for the check:
        -> [(-1, 0), (1, 0), (0, -1), (0, 1)]"""
        raise NotImplementedError

    @staticmethod
    def in_bounds(grid, r, c):
        """Is (r, c) inside the grid.   (GRID, 3, 0) -> False"""
        raise NotImplementedError

    @staticmethod
    def neighbours(grid, r, c):
        """In-bounds orthogonal neighbour coordinates of (r, c), in the direction
        order above.   (GRID, 0, 0) -> [(1, 0), (0, 1)]"""
        raise NotImplementedError


class Turn:
    """Transpose and rotate, via the * spread into zip."""

    @staticmethod
    def transpose(grid):
        """Rows become columns, as LISTS not tuples.
        -> [[1, 0, 0], [1, 1, 0], [0, 0, 1]]"""
        raise NotImplementedError

    @staticmethod
    def rotate_cw(grid):
        """90 degrees clockwise.   -> [[0, 0, 1], [0, 1, 1], [1, 0, 0]]"""
        raise NotImplementedError

    @staticmethod
    def rotate_cw_in_place(grid):
        """Same rotation, but the caller's list object must be the one that changes.
        Return it.   -> [[0, 0, 1], [0, 1, 1], [1, 0, 0]]"""
        raise NotImplementedError


def _g():
    return [row[:] for row in GRID]


CHECKS = [
    ("dims",                lambda: Shape.dims(_g()), (3, 3)),
    ("count of 1",          lambda: Shape.count_value(_g(), 1), 4),
    ("flatten",             lambda: Shape.flatten(_g()), [1, 1, 0, 0, 1, 0, 0, 0, 1]),

    ("zeros 2x3",           lambda: Build.zeros(2, 3), [[0, 0, 0], [0, 0, 0]]),
    ("deep copy",           lambda: Build.deep_copy(_g()), [[1, 1, 0], [0, 1, 0], [0, 0, 1]]),
    ("aliasing proof",      lambda: Build.aliased_proof(2, 3), [[9, 0, 0], [9, 0, 0]]),

    ("directions",          lambda: Move.directions(), [(-1, 0), (1, 0), (0, -1), (0, 1)]),
    ("in bounds (3,0)",     lambda: Move.in_bounds(_g(), 3, 0), False),
    ("neighbours of (0,0)", lambda: Move.neighbours(_g(), 0, 0), [(1, 0), (0, 1)]),

    ("transpose",           lambda: Turn.transpose(_g()), [[1, 0, 0], [1, 1, 0], [0, 0, 1]]),
    ("rotate cw",           lambda: Turn.rotate_cw(_g()), [[0, 0, 1], [0, 1, 1], [1, 0, 0]]),
    ("rotate cw in place",  lambda: Turn.rotate_cw_in_place(_g()), [[0, 0, 1], [0, 1, 1], [1, 0, 0]]),
]

if __name__ == "__main__":
    run(CHECKS, "grids.py")
