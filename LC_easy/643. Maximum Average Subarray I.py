class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        array = nums[:k]
        current_sum = max_sum = sum(array)

        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]  # Add new right element, remove old left element

            max_sum = max(max_sum, current_sum)

        return max_sum / k  # Only the max_sum from all iterations needed when calculating average


if __name__ == "__main__":
    s = Solution()
    assert s.findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4) == 12.75000


"""
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
Any answer with a calculation error less than 10-5 will be accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000
 
Constraints:
n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
"""