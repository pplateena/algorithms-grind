"""
Recursion Algorith calls itself with smaller values each run and returns result for the last input.
"""
def Recursion_base(searched_object: list, target, index: int = None, print = False) -> int or None:
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
        if print: print(f"Target value {target} found, under index {index} in object:\n{searched_object}\n")
        return index
    elif index == 0: # List has ended and we didn't find target
        if print: print(f"Target value {target} wasn't found in object:\n{searched_object}")
        return None
    else: # Recursive state
        Recursion_base(searched_object, target, index - 1)

""" Returns sum of all values of given list """
def Sum_recursion(nums: list[int], in_place: bool = False) -> int:
    """in_place destroys the inputted list and returns the sum"""
    match in_place:
        case False:
            if len(nums) == 1:
                return nums[0]
            else:
                return nums[-1] + Sum_recursion(nums[:-1]);
        case True:
            if len(nums) == 1:
                return nums.pop()
            else:
                return nums.pop(-1) + Sum_recursion(nums, True)

""" Returns maximum value of given list """
def Max_recursion(nums: list[int], index: int = None) -> int:
    if index is None:
        index = len(nums) - 1

    if index == 0:
        return nums[0]
    else:
        return max(nums[index], Max_recursion(nums, index - 1))

""" Same logic as Base Recursion but, utilizes Binary Search algorithm, dividing list by 2 each recursion """
def Binary_recursion(nums: list[int], target: int, low: int = None, high: int = None) -> int:
    """

    :param nums: list[int], required to be sorted
    :param target: int, number we are searching for
    :param low: int, index of lower bound of the searching window
    :param high: int, index of upper bound of the searching window
    :return: int, index of searched element in a given list, or None if target is not found
    """
    if low is None or high is None:
        low, high = 0, len(nums) - 1

    mid = (low + high) // 2

    if nums[mid] == target:
        return mid
    elif low == high:
        return None
    elif nums[mid] > target:
        return Binary_recursion(nums, target, low, mid - 1)
    else:
        return Binary_recursion(nums, target, mid + 1, high)



""" Custom dataclass using built-in decorator for pretty tests """
from dataclasses import dataclass, field
from random import randint, choice, randrange, shuffle
import timeit
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

    BASIC = True
    SUM = True
    MAX = True
    BINARY = True
    if BASIC:
        print("Starting Basic Recursion on this testcase:")
        testCase = Dataset()
        print(testCase)
        Recursion_base(testCase.nums, choice(testCase.nums))

    if SUM:
        print("Starting Sum Recursion on this testcase:")
        testCase = Dataset()
        print(testCase.nums)
        print(Sum_recursion(testCase.nums))
        time_slicing = timeit.timeit('Sum_recursion(testCase.nums)',
                              setup='from __main__ import Sum_recursion, testCase',
                              number=1)

        time_pop = timeit.timeit('Sum_recursion(testCase.nums, True)',
                              setup='from __main__ import Sum_recursion, testCase',
                              number=1)

        print(f"Time for sum_recursion(testCase.nums): {time_slicing} seconds")
        print(f"Time for sum_recursion(testCase.nums, True): {time_pop} seconds")

    if MAX:
        print("Starting Max Recursion on this testcase:")
        testCase = Dataset()
        print(testCase.nums)
        print(Max_recursion(testCase.nums))

    if BINARY:
        testCase = Dataset()
        testCase.nums = sorted(testCase.nums)
        target = choice(testCase.nums)
        print(f"Starting Binary Recursion Search for target '{target}' on this testcase:")
        print(testCase.nums)
        print(Binary_recursion(testCase.nums, target))

        time_defult = timeit.timeit('Recursion_base(testCase.nums, target)',
                              setup='from __main__ import Recursion_base, testCase, target',
                              number=10000)

        time_binary = timeit.timeit('Binary_recursion(testCase.nums, target)',
                              setup='from __main__ import Binary_recursion, testCase, target',
                              number=10000)

        print(f"Time for Basic_recursion(testCase.nums, {target})': {time_defult} seconds")
        print(f"Time for Binary_recursion(testCase.nums, {target}): {time_binary} seconds")
        print('default / binary = ', time_defult / time_binary)