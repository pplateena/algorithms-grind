"""Strings — typing recall.

Strings are immutable: nothing here changes S, everything returns a new object.
Run:  python3 strings.py
"""
from drill import run

S = "the quick brown fox jumps"
T, U = "Listen", "silent"


class Parts:
    """Splitting and rejoining."""

    # Need a brief on inplace - copy differences for string methods
    @staticmethod
    def words(s):
        """-> ['the', 'quick', 'brown', 'fox', 'jumps']"""
        return s.split()

    @staticmethod
    def joined(words, sep):
        """(['a','b'], '-') -> 'a-b'"""

        # do not remember how to do it differently, pretty sure it can be done not
        # via "".join(list)
        return sep.join(words)

    @staticmethod
    def no_spaces(s):
        """-> 'thequickbrownfoxjumps'"""

        # don't remember how to delete, but replace should work here fine
        return s.replace(" ", "")

    @staticmethod
    def reversed_string(s):
        """-> 'spmuj xof nworb kciuq eht'"""

        # I don't know if slicing can reverse similar to lists [::-1], but we can sort + join
        return "".join(reversed(s))

    @staticmethod
    def sorted_chars(s):
        """The characters of a word in order, AS A STRING.
        Note what sorted() hands back before you join it.   ('eat') -> 'aet'"""

        # Sorted returns list ov strings, not str

        return "".join(sorted(s))


class Chars:
    """Single characters and the alphabet."""

    @staticmethod
    def alpha_index(c):
        """Position in the alphabet, a=0.   ('c') -> 2"""
        char_alphabet_pos = ord(c) - ord('a')
        print(c, ord(c), ord('a'), chr(97), ord(" "))
        return char_alphabet_pos

    @staticmethod
    def char_at(i):
        """The letter at alphabet position i.   (25) -> 'z'"""
        return chr(ord('a') + i)

    @staticmethod
    def count_char(s, c):
        """How many c in s.   (S, 'o') -> 2"""
        total, desired_ord = 0, ord(c)
        for val in s:
            if ord(val) == desired_ord:
                total += 1

        # i am not sure whether this is correct approach, i want to know how to do
        # it correctly as well as how to do it in single line
        return total

    @staticmethod
    def is_alnum(s):
        """Are ALL characters alphanumeric (a space is not).   (S) -> False"""

        # idk how to check it via ord/chr, i tested that ord(" ") -> 32, okay i
        # figured how to do it, but it's not optimal for sure

        return s.isalnum()
class Find:
    """Locating substrings. One of these raises, the other does not — know which."""

    @staticmethod
    def index_of(s, sub):
        """Where sub starts.   (S, 'brown') -> 10"""
        return s.find(sub) # need brief on how find() works, just guessed this code

    @staticmethod
    def index_or_missing(s, sub):
        """Where sub starts, or -1 when absent, WITHOUT raising.   (S, 'cat') -> -1"""

        # if sub in s:
        #     return s.find(sub) # need brief on how find() works, just guessed this code

        # return -1
        return s.find(sub)

    @staticmethod
    def ends_with(s, suffix):
        """(S, 'jumps') -> True"""

        # if s.endswith(suffix):
        #     return True
        # return False
        return s.endswith(suffix)
    @staticmethod
    def report(s, sub):
        """An f-string: 'fox appears at 16' — compute the 16.   (S, 'fox')"""
        return f'{sub} appears at {s.find(sub)}'

class Compare:
    """Equality up to rearrangement or case."""

    @staticmethod
    def anagram_sorted(a, b):
        """Case-insensitive, via sorting.   ('Listen', 'silent') -> True"""

        if sorted(a.lower()) == sorted(b.lower()):
            return True
        return False

    @staticmethod
    def anagram_counter(a, b):
        """Same answer, via Counter.   -> True"""

        # not sure whether this would work but i would like to try ord + lower + sum

        # only usable with bucket = [0]*26
        # a_count = 0
        # b_count = 0

        # for c in a.lower():
        #     a_count += ord(c)

        # for c in b.lower():
        #     b_count += ord(c)
        #     if b_count > a_count:
        #         return False
        from collections import Counter
        return Counter(a.lower()) == Counter(b.lower())


    @staticmethod
    def equal_ignoring_case(a, b):
        """('Fig', 'fig') -> True"""

        return True if a.lower() == b.lower() else False

        # can be done via char counts as well i guess, same to prev


CHECKS = [
    ("words",              lambda: Parts.words(S), ['the', 'quick', 'brown', 'fox', 'jumps']),
    ("joined with dash",   lambda: Parts.joined(S.split(), '-'), 'the-quick-brown-fox-jumps'),
    ("no spaces",          lambda: Parts.no_spaces(S), 'thequickbrownfoxjumps'),
    ("reversed",           lambda: Parts.reversed_string(S), 'spmuj xof nworb kciuq eht'),
    ("sorted chars",       lambda: Parts.sorted_chars("eat"), 'aet'),

    ("alpha index of c",   lambda: Chars.alpha_index('c'), 2),
    ("char at 25",         lambda: Chars.char_at(25), 'z'),
    ("count of o",         lambda: Chars.count_char(S, 'o'), 2),
    ("is alnum",           lambda: Chars.is_alnum(S), False),

    ("index of brown",     lambda: Find.index_of(S, 'brown'), 10),
    ("index of cat",       lambda: Find.index_or_missing(S, 'cat'), -1),
    ("ends with jumps",    lambda: Find.ends_with(S, 'jumps'), True),
    ("f-string report",    lambda: Find.report(S, 'fox'), 'fox appears at 16'),

    ("anagram via sorted", lambda: Compare.anagram_sorted(T, U), True),
    ("anagram via Counter", lambda: Compare.anagram_counter(T, U), True),
    ("equal ignoring case", lambda: Compare.equal_ignoring_case('Fig', 'fig'), True),
]

if __name__ == "__main__":
    run(CHECKS, "strings.py")
