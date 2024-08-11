
class Solution:
    def __init__(self, nums):
        self.nums = nums
        self.moveZeroes(self.nums)

    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        l = len(nums)

        if l == 1:
            return

        while low < l:

            if nums[low] == 0:
                high = low + 1

                while high < l:
                    if nums[high] != 0:
                        nums[low], nums[high] = nums[high], nums[low]
                        low += 1
                        break
                    else:
                        high += 1
                        if high == l:
                            return
                else:
                    return
            else:
                low += 1

if __name__ == "__main__":
    tests = [[[0,1,0,3,12], [1,3,12,0,0]], [[0,1], [1,0]], [[1,0], [1,0]], [[0,0], [0,0]], [[1,1],[1,1]]]
    for test in tests:
        input_test, output_test = test[0], test[1]
        assert Solution(input_test).nums == output_test




"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of 
the non-zero elements. Note that you must do this in-place without making a copy of the array.

 

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
 

Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 
"""