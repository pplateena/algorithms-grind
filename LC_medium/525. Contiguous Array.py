class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        seen = {0: -1}
        ones = zeros = max_found = 0

        for idx, n in enumerate(nums):
            if n == 0:
                zeros += 1
            else:
                ones += 1

            target = zeros - ones
            if target in seen:
                max_found = max(max_found, idx - seen[target])
            else:
                seen[target] = idx

        return max_found


if __name__ == "__main__":
    s = Solution()
    assert s.findMaxLength(nums = [0,1,1,1,1,1,0,0,0]) == 6
    assert s.findMaxLength(nums = [0,1,0]) == 2
    assert s.findMaxLength([0,1]) == 2

"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Example 3:

Input: nums = [0,1,1,1,1,1,0,0,0]
Output: 6
Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""