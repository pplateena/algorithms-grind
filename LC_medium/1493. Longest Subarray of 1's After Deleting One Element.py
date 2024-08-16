class Solution:
    def longestSubarray(self, nums: list[int]) -> int:

        current, previous = 0, 0
        answer = 0

        for number in nums:
            if number == 1:
                current += 1
            else:
                answer = max(answer, current + previous)
                previous = current  # in new cycle we would need to connect both answers, because thay may contain
                # only 1 zero between them
                current = 0  # we start anew, because found 0

        answer = answer = max(answer, current + previous)  # in case last is zero
        return answer - 1 if answer == len(nums) else answer


if __name__ == "__main__":
    s = Solution()
    assert s.longestSubarray([1,1,0,1]) == 3
    assert s.longestSubarray([0,1,1,1,0,1,1,0,1]) == 5
    assert s.longestSubarray([1,1,1]) == 2


"""
Given a binary array nums, you should delete one element from it.
Return the size of the longest non-empty subarray containing only 1's in the resulting array. 
Return 0 if there is no such subarray.

Example 1:
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 
Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""