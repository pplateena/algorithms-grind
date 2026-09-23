class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        seen = {}
        total = counter = 0
        seen[0] = 1

        for n in nums:
            total += n

            counter += seen.get(total-k, 0)
            seen[total] = seen.get(total, 0) + 1

        return counter

if __name__ == "__main__":
    s = Solution()

    assert s.subarraySum([1,-1,0,1,-1], 0) == 7
    assert s.subarraySum(nums = [1,2,3], k = 3) == 2
    assert s.subarraySum(nums = [1,1,1], k = 2) == 2

"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 
Constraints:
1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""