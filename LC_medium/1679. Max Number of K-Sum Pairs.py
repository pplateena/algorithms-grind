class Solution:
    def maxOperations_hashMap(self, nums: list[int], k: int) -> int:
        """ Beats 21% Runtime """
        from collections import defaultdict

        nums_dict = defaultdict(int)
        counter = 0

        for number in nums:

            if k - number in nums_dict and nums_dict[k - number] > 0:
                nums_dict[k - number] -= 1
                counter += 1

            else:
                nums_dict[number] += 1

        return counter


    def maxOperations_twoPointers(self, nums: list[int], k: int) -> int:
        """ Beats 70% Runtime """

        nums.sort()
        i, j = 0, len(nums) - 1
        counter = 0
        while i < j:
            target = nums[i] + nums[j]
            if target == k:
                counter += 1
                i += 1
                j -= 1
            elif target > k:
                j -= 1
            else:
                i += 1

        return counter

if __name__ == "__main__":
    s = Solution()
    assert s.maxOperations_hashMap(nums = [1,2,3,4], k = 5) == 2
    assert s.maxOperations_twoPointers(nums = [3,1,3,4,3], k = 6) == 1


"""
You are given an integer array nums and an integer k.
In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
Return the maximum number of operations you can perform on the array.

Example 1:
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

Example 2:
Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
 
Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
"""