"""Bits — typing recall. Grows with each lesson; today covers steps 1–2
(binary representation; &, |, ^).

Run:  python3 bits.py
"""
from drill import run


class Convert:
    """Between ints and binary strings."""

    @staticmethod
    def to_binary(n):
        """With the prefix.   13 -> '0b1101'"""
        raise NotImplementedError

    @staticmethod
    def to_binary_digits(n):
        """Digits only, no prefix.   13 -> '1101'"""
        raise NotImplementedError

    @staticmethod
    def padded(n, width):
        """Zero-padded to a fixed width.   (5, 8) -> '00000101'"""
        raise NotImplementedError

    @staticmethod
    def from_binary(s):
        """Binary string to int.   '1101' -> 13"""
        raise NotImplementedError

    @staticmethod
    def literal():
        """Return thirteen, written as a binary literal in the source.   -> 13"""
        raise NotImplementedError


class Ops:
    """The three column-by-column operators."""

    @staticmethod
    def both(a, b):
        """Bits set in both.   (13, 6) -> 4"""
        raise NotImplementedError

    @staticmethod
    def either(a, b):
        """Bits set in at least one.   (13, 6) -> 15"""
        raise NotImplementedError

    @staticmethod
    def differ(a, b):
        """Bits where they differ.   (13, 6) -> 11"""
        raise NotImplementedError

    @staticmethod
    def last_bit(n):
        """The lowest bit, by masking — not %.   13 -> 1"""
        raise NotImplementedError

    @staticmethod
    def is_odd(n):
        """True/False, by masking — not %.   6 -> False"""
        raise NotImplementedError


CHECKS = [
    ("to binary 13",        lambda: Convert.to_binary(13), '0b1101'),
    ("digits only 13",      lambda: Convert.to_binary_digits(13), '1101'),
    ("padded 5 to 8",       lambda: Convert.padded(5, 8), '00000101'),
    ("from '1101'",         lambda: Convert.from_binary('1101'), 13),
    ("literal 13",          lambda: Convert.literal(), 13),

    ("13 & 6",              lambda: Ops.both(13, 6), 4),
    ("13 | 6",              lambda: Ops.either(13, 6), 15),
    ("13 ^ 6",              lambda: Ops.differ(13, 6), 11),
    ("last bit of 13",      lambda: Ops.last_bit(13), 1),
    ("is 6 odd",            lambda: Ops.is_odd(6), False),
    ("is 13 odd",           lambda: Ops.is_odd(13), True),
]

if __name__ == "__main__":
    run(CHECKS, "bits.py")
