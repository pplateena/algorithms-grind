"""
Recursion Algorith calls itself with smaller values each run and returns result for the last input.
"""
def Recursion(searched_object: list, target, index: int = None ) -> int or None:
    """
    :param searched_object: list of any values that can be compared, for example int or str
    :param target: int or str, the value which is being searched inside list
    :return: searched_object.index(target): int or None
    """

    """
    Upon first initialisation, we don't know position of last element, in order not to invoke len() each 
    time we use the recursion function, we can check whether index variable is passed, if not we take the len(list)
    """

    if index is None:
        index = len(searched_object) - 1

    """
    Recursion has two states:
        Basic - we matched our condition
        Recursive - we didn't match our condition, and we can continue checking values deeper in a list, e.g. 
        we didn't reached 0 index.
    We simply finish the function if we get to basic state, returning index or boolean, otherwise we call 
    function again, excluding all previously checked values. As well we gotta check whether we reached index 0 to not
    end up in endless loop, if we reached it and value isn't our target, we return False or None like in this example.
    """
    if searched_object[index] == target: # Basic state
        print(f"Target value {target} found, under index {index} in object:\n{searched_object}\n")
        return index
    elif index == 0: # List has ended and we didn't find target
        print(f"Target value {target} wasn't found in object:\n{searched_object}")
        return None
    else: # Recursive state
        Recursion(searched_object, target, index - 1)


"""Custom dataclass using built-in decorator for pretty tests"""
from dataclasses import dataclass, field
from random import randint, choice, randrange, shuffle
def generate_nums():
    return [randrange(0,78) for _ in range(randint(1,20))]
def generate_text():
    words_list = ("Hello World! sdgasd gasetdfas HJUSBAGDF help me. Please, tell me your number, I love crack. See you soon!!").split()
    shuffle(words_list)
    return words_list
@dataclass
class Dataset:
    nums: list[int] = field(default_factory = generate_nums)
    text: list[str] = field(default_factory = generate_text)


if __name__ == "__main__":
    for n in range(2):
        testCase = Dataset()
        Recursion(testCase.nums, choice(testCase.nums))
        Recursion(testCase.text, choice(testCase.text))
