class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        storage_set = set(nums) # deals with duplicates and makes compute faster
        longest_found = 0 # initializing longest value storage
        """
        If we rearrange the wording, our task is to find a sequences and return len() of the longest.
        To understand whether we are working with the start of possible sequence, we can check if in the 
        storage_set there is 'start_number - 1'. 
        When there are no previous consequent values in set, we can be sure that we are at the start of the sequence,
        and now we can use simple incrementation when sequence contains another number, until there is none.
        """
        for start_number in storage_set:
            if start_number - 1 not in storage_set:
                end_number = start_number + 1

                while end_number in storage_set:
                    end_number += 1

                longest_found = max(longest_found, end_number - start_number)

        return longest_found

if __name__ == "__main__":

    s = Solution()
    assert s.longestConsecutive([100,4,200,1,3,2]) == 4
    assert s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9

"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""