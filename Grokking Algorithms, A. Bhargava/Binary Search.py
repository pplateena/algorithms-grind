"""
Binary Search is very useful technique which provides O(log n) time complexity for working with sorted arrays of
numbers. It can be used in various tasks, often implemented in other algorithms to speed up the process.
"""
def binary_search(sorted_list:list[int], target: int) -> int:
    """
    :param sorted_list: list of integers, has to be sorted from smallest to largest
    :param target: int, the number we want to find inside the list
    :return: searched_list.index(target), we return index value of searched item, target
    """

    low, high = 0, len(sorted_list) - 1

    """ We break the loop if any of pointers are not in order or out of borders """
    while low <= high:

        mid = (low + high) // 2 # Floor division to never skip a value, which can happen with default division
        guess = sorted_list[mid]

        if guess == target:
            return mid
        elif guess > target:
            """
            If guess is greater than target, then we can safely assume that in sorted list, all values
            to the right of middle are greater as well, also decrement by 1 to get rid of middle value.
            """
            high = mid - 1
        else:
            """
            Because we handled equals and higher cases, the only remaining case is guess is lower than
            target. We proceed with same logic, but now we move left border and exclude guess by incrementing.
            We can say that this works as sort of slicing the list, but only with indices, "nums = [mid + 1:]",
            but with big benefit of O(1), because default slicing is always O(k), where k is list size
            """
            low = mid + 1
    """If our loop finished without any return, searched element is not presented in the list, and we return None"""

    return None

def Binary_recursion(nums: list[int], target: int, low: int = None, high: int = None) -> int:

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
def generate_test():
    from random import randint
    generated_list = sorted([randint(0,25) for _ in range(randint(0,15))])

    generated_target = generated_list[randint(0, len(generated_list) - 1)] if len(generated_list) > 0 else 1

    print(f'Generated\nNew list: {generated_list}\nTarget: {generated_target}')
    return generated_list, generated_target

if __name__ == "__main__":


    assert binary_search([1, 2, 3, 4, 5, 6, 7, 8], 8) == 7

    rand_list, rand_target = generate_test()

    print("Binary search output", binary_search(rand_list, rand_target))