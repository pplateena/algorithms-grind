"""Dicts — typing recall.

Run:  python3 dicts.py
"""
from drill import run

D = {'a': 3, 'b': 1, 'c': 2}
WORDS = ['pear', 'apple', 'pear', 'fig', 'apple', 'pear']


class Access:
    """Reading and writing single keys. Membership and lookup are both O(1)."""

    @staticmethod
    def get_default(d, k, default):
        """Value of k, or default when absent — no KeyError.   (D, 'z', 0) -> 0"""
        return d.get(k, default)

    @staticmethod
    def increment(d, k):
        """Add 1 to d[k], starting from 0 when absent. Return the dict.
        (D, 'z') -> {'a':3, 'b':1, 'c':2, 'z':1}"""
        d[k] = d.get(k, 0) +1
        return d

    @staticmethod
    def has_key(d, k):
        """(D, 'b') -> True   — note what `in` iterates over for a dict"""

        return k in d

    @staticmethod
    def without(d, k):
        """Delete k, return the dict.   (D, 'b') -> {'a': 3, 'c': 2}"""
        del d[k]
        return d

    @staticmethod
    def pop_default(d, k, default):
        """Remove k and return its value, or default when absent.   (D, 'z', 0) -> 0"""
        return d.pop(k, default)


class Order:
    """Dicts keep insertion order; any other order you ask for explicitly."""

    @staticmethod
    def items_by_value_desc(d):
        """-> [('a', 3), ('c', 2), ('b', 1)]"""
        return sorted(d.items(), key= lambda kv: kv[1], reverse = True)

    @staticmethod
    def key_with_max_value(d):
        """-> 'a'   (the KEY, not the value — think about what key= receives)"""
        return max(d, key = d.get)
        return sorted(d.items(), key = lambda kv: kv[1], reverse = True)[:1][0][0]

    @staticmethod
    def keys_sorted(d):
        """-> ['a', 'b', 'c']"""
        return sorted(d)


class Transform:
    """Dict comprehensions: {k_expr: v_expr for k, v in d.items()}."""

    @staticmethod
    def doubled(d):
        """-> {'a': 6, 'b': 2, 'c': 4}"""

        return {k: v*2 for k, v in d.items()}

    @staticmethod
    def inverted(d):
        """Value becomes the key.   -> {3: 'a', 1: 'b', 2: 'c'}"""

        # items = [n for n in d.items()]

        # for n in items:
        #     d[n[1]] = n[0]
        #     del d[n[0]]

        # return d # i don't think this is good solution
        return {v: k for k, v in d.items()}


    @staticmethod
    def from_pairs(pairs):
        """([('a',1), ('b',2)]) -> {'a': 1, 'b': 2}"""
        # d = {}
        # for n in pairs:
        #     d[n[0]] = n[1]
        # return d
        return {k: v for k, v in pairs}

class Counting:
    """Frequency tables. Counter is a dict subclass, so it compares equal to one."""

    @staticmethod
    def frequency(items):
        """A dict of counts (a Counter or defaultdict passes too).   -> {'pear': 3, 'apple': 2, 'fig': 1}"""
        # from collections import defaultdict
        # d = defaultdict(int)
        # for n in items:
        #     d[n] += 1
        # print(d.items())

        # d = {}
        # for n in items:
        #     if n in d:
        #         d[n] += 1
        #     else:
        #         d[n] = 1
        # return d
        from collections import Counter
        d = Counter(items)
        print(d)
        return d

    @staticmethod
    def top_two(items):
        """The two commonest, with counts.   -> [('pear', 3), ('apple', 2)]"""
        # d = {}
        # for n in items:
        #     if n in d:
        #         d[n] += 1
        #     else:
        #         d[n] = 1

        # sort by value, idk how
        from collections import defaultdict
        d = defaultdict(int)
        for n in items:
            d[n] += 1

        return sorted(d.items(), key = lambda kv: kv[1], reverse = True)[:2]

    @staticmethod
    def bucket_by_length(words):
        """Group words by length, using a defaultdict.
        (['fig','pear','plum']) -> {3: ['fig'], 4: ['pear', 'plum']}"""
        d = {}
        for n in words:
            l = len(n)
            if l in d:
                d[l].append(n)
            else:
                d[l] = [n]
        return d

class Iterate:
    """Looping. items() gives pairs; keys() and values() give views, not lists."""

    @staticmethod
    def sum_values(d):
        """-> 6"""
        return sum(d.values())

    @staticmethod
    def keys_list(d):
        """A real list, not a view.   -> ['a', 'b', 'c']"""
        return list(d.keys())

    @staticmethod
    def values_list(d):
        """-> [3, 1, 2]"""
        return list(d.values())
        return [n for n in d.values()]

    @staticmethod
    def pairs_where(d, limit):
        """Keys whose value > limit.   (D, 1) -> ['a', 'c']"""
        return [k for k, v in d.items() if v > limit]


CHECKS = [
    ("get with default",    lambda: Access.get_default(dict(D), 'z', 0), 0),
    ("increment missing",   lambda: Access.increment(dict(D), 'z'), {'a': 3, 'b': 1, 'c': 2, 'z': 1}),
    ("has key b",           lambda: Access.has_key(dict(D), 'b'), True),
    ("delete b",            lambda: Access.without(dict(D), 'b'), {'a': 3, 'c': 2}),
    ("pop missing",         lambda: Access.pop_default(dict(D), 'z', 0), 0),

    ("items by value desc", lambda: Order.items_by_value_desc(dict(D)), [('a', 3), ('c', 2), ('b', 1)]),
    ("key with max value",  lambda: Order.key_with_max_value(dict(D)), 'a'),
    ("keys sorted",         lambda: Order.keys_sorted(dict(D)), ['a', 'b', 'c']),

    ("doubled values",      lambda: Transform.doubled(dict(D)), {'a': 6, 'b': 2, 'c': 4}),
    ("inverted",            lambda: Transform.inverted(dict(D)), {3: 'a', 1: 'b', 2: 'c'}),
    ("from pairs",          lambda: Transform.from_pairs([('a', 1), ('b', 2)]), {'a': 1, 'b': 2}),

    ("frequency",           lambda: Counting.frequency(list(WORDS)), {'pear': 3, 'apple': 2, 'fig': 1}),
    ("top two",             lambda: Counting.top_two(list(WORDS)), [('pear', 3), ('apple', 2)]),
    ("bucket by length",    lambda: Counting.bucket_by_length(['fig', 'pear', 'plum']), {3: ['fig'], 4: ['pear', 'plum']}),

    ("sum of values",       lambda: Iterate.sum_values(dict(D)), 6),
    ("keys as list",        lambda: Iterate.keys_list(dict(D)), ['a', 'b', 'c']),
    ("values as list",      lambda: Iterate.values_list(dict(D)), [3, 1, 2]),
    ("keys where value>1",  lambda: Iterate.pairs_where(dict(D), 1), ['a', 'c']),
]

if __name__ == "__main__":
    run(CHECKS, "dicts.py")
