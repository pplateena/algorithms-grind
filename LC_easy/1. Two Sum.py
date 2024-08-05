class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        set_nums = set(nums)

        for number in nums:
            looking_for = target - number
            if looking_for in set_nums:

                if looking_for == number and nums.count(number) == 1:
                    continue

                first_i, second_i = nums.index(number), nums.index(looking_for)

                if first_i == second_i:
                    first_i = nums.index(number)
                    nums.pop(first_i)
                    second_i = nums.index(looking_for) + 1

                return [first_i, second_i]


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