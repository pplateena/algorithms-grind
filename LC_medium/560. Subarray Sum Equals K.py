class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # left = 0
        # while left < l:
        #     # sub_array = [nums[left]]
        #     total = nums[left]
        #     if total == k:
        #         counter += 1
        #         # left += 1

        #     # else:
        #     right = left + 1
        #     while right < l:
        #         # sub_array.append(nums[right])
        #         total += nums[right]
        #         if total == k:
        #             counter += 1
        #         right += 1

        #     left += 1

        # if sum(nums) == k:
        #     counter += 1

        counter = 0
        l = len(nums)

        if l < 2:
            return 1 if sum(nums) == k else 0

        for left in range(l):

            total = nums[left]
            if total == k:
                counter += 1

            for right in range(left + 1, l):

                total += nums[right]
                if total == k:
                    counter += 1

        return counter
if __name__ == "__main__":
    s = Solution()

    assert s.subarraySum([1,-1,0,1,-1], 0) == 5
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