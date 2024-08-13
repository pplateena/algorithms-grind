class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        counters_dict = {}

        for number in set(arr):
            counter = 0
            while number in arr:
                counter += 1
                arr.pop(arr.index(number))

            if counter in counters_dict:
                return False
            else:
                counters_dict[counter] = number

        return True


if __name__ == "__main__":
    s = Solution()
    assert s.uniqueOccurrences(arr = [1,2,2,1,1,3]) == True
    assert s.uniqueOccurrences(arr = [1,2]) == False
    assert s.uniqueOccurrences(arr = [-3,0,1,-3,1,1,1,-3,10,0]) == True


"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false 
otherwise.

Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:
Input: arr = [1,2]
Output: false

Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 
Constraints:
1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
"""