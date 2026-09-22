"""lambda — typing recall.

A lambda is an expression whose value is a function. Body = ONE expression:
no assignment, no loops, no `return`. A ternary is allowed. Never name one —
its job is to be passed inline, almost always to `key=`.

Model for key=: given ONE element, what value should be compared in its place?
Python calls it once per element and returns the ORIGINAL elements, reordered.

Run:  python3 lambdas.py
"""
from drill import run

PAIRS = [('pear', 3), ('apple', 2), ('fig', 5)]
WORDS = ['bb', 'a', 'ccc', 'dd']
PTS = [(1, 2), (3, 1), (-2, 0)]
MIXED = ['Fig', 'apple', 'Pear']


class Key:
    """Where lambdas actually go: sorted / sort / max / min / nlargest."""

    @staticmethod
    def by_count_desc(pairs):
        """-> [('fig',5), ('pear',3), ('apple',2)]"""
        raise NotImplementedError

    @staticmethod
    def by_length_then_alpha(words):
        """-> ['a', 'bb', 'dd', 'ccc']"""
        raise NotImplementedError

    @staticmethod
    def max_by_count(pairs):
        """The PAIR with the largest count, not the count.   -> ('fig', 5)"""
        raise NotImplementedError

    @staticmethod
    def by_distance(pts):
        """Nearest the origin first, no sqrt.   -> [(-2,0), (1,2), (3,1)]"""
        raise NotImplementedError

    @staticmethod
    def by_length_desc_then_alpha(words):
        """Length descending, name ascending. The real test: length negates,
        the string cannot.   -> ['ccc', 'bb', 'dd', 'a']"""
        raise NotImplementedError


class NoLambda:
    """When the function already exists, pass it BARE. `key=lambda s: len(s)` is noise."""

    @staticmethod
    def by_length(words):
        """No lambda.   -> ['a', 'bb', 'dd', 'ccc']"""
        raise NotImplementedError

    @staticmethod
    def case_insensitive(words):
        """No lambda.   -> ['apple', 'Fig', 'Pear']"""
        raise NotImplementedError

    @staticmethod
    def by_magnitude(nums):
        """No lambda.   ([3,-7,2]) -> [2, 3, -7]"""
        raise NotImplementedError


class Factory:
    """defaultdict takes a ZERO-argument callable. A bare type needs no lambda;
    anything else does."""

    @staticmethod
    def default_minus_one(key):
        """A defaultdict whose missing value is -1; return d[key].   -> -1"""
        raise NotImplementedError

    @staticmethod
    def default_three_zeros(key):
        """A defaultdict whose missing value is a fresh [0, 0, 0]; return d[key].
        -> [0, 0, 0]"""
        raise NotImplementedError


class TwoArg:
    """The ONE place a sorting lambda takes two arguments. Returns neg / 0 / pos."""

    @staticmethod
    def cmp_sorted(nums):
        """Sort ascending via functools.cmp_to_key.   ([3,1,2]) -> [1, 2, 3]"""
        raise NotImplementedError


class Gotcha:
    """Late binding: a lambda looks up free variables when it RUNS, not when built."""

    @staticmethod
    def broken():
        """Build [lambda: i for i in range(3)], call all three, return the results.
        -> [2, 2, 2]   (yes, that is the correct expected value)"""
        raise NotImplementedError

    @staticmethod
    def fixed():
        """Same list, one token changed so each captures its own i.   -> [0, 1, 2]"""
        raise NotImplementedError


CHECKS = [
    ("by count desc",          lambda: Key.by_count_desc(list(PAIRS)), [('fig', 5), ('pear', 3), ('apple', 2)]),
    ("length then alpha",      lambda: Key.by_length_then_alpha(list(WORDS)), ['a', 'bb', 'dd', 'ccc']),
    ("max by count",           lambda: Key.max_by_count(list(PAIRS)), ('fig', 5)),
    ("by distance, no sqrt",   lambda: Key.by_distance(list(PTS)), [(-2, 0), (1, 2), (3, 1)]),
    ("len desc then alpha",    lambda: Key.by_length_desc_then_alpha(list(WORDS)), ['ccc', 'bb', 'dd', 'a']),

    ("by length, no lambda",   lambda: NoLambda.by_length(list(WORDS)), ['a', 'bb', 'dd', 'ccc']),
    ("case-insensitive",       lambda: NoLambda.case_insensitive(list(MIXED)), ['apple', 'Fig', 'Pear']),
    ("by magnitude",           lambda: NoLambda.by_magnitude([3, -7, 2]), [2, 3, -7]),

    ("default -1",             lambda: Factory.default_minus_one('z'), -1),
    ("default [0,0,0]",        lambda: Factory.default_three_zeros('z'), [0, 0, 0]),

    ("cmp_to_key ascending",   lambda: TwoArg.cmp_sorted([3, 1, 2]), [1, 2, 3]),

    ("late binding, broken",   lambda: Gotcha.broken(), [2, 2, 2]),
    ("late binding, fixed",    lambda: Gotcha.fixed(), [0, 1, 2]),
]

if __name__ == "__main__":
    run(CHECKS, "lambdas.py")
