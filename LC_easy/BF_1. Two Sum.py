class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_set = nums
        loop_range = nums.copy()

        for i in loop_range:
            nums_set.pop(0)

            for number in nums_set:
                # print(nums_set)
                if number <= 0 and i <= 0 and target > 0:
                    continue
                if number + i == target:

                    output = [loop_range.index(number), loop_range.index(i)]

                    if output[0] == output[1]:
                        output = [i for i in range(len(loop_range)) if loop_range[i] == number]

                        if len(output) > 2:
                            output = output[1:2]

                    return output


if __name__ == "__main__":
    s = Solution()
    assert s.twoSum([3,2,4], 6) == [1,2] or [2,1]
    assert s.twoSum([2,7,11,15], 9) == [0, 1] or [1,0]
    assert s.twoSum([3,3], 6) == [0,1] or [1, 0]


"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""