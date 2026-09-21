class Solution:

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # DOESN'T PASS RUNTIME
        # if len(nums) < 2:
        #     return False

        # uniq = set(nums)
        # if len(uniq) == 1:
        #     return True

        # for n in uniq:
        #     if nums.count(n) > 1:
        #         return True

        # return False

        # if len(nums) < 2:
        #     return False
        uniq = set()

        for n in nums:
            if n in uniq:
                return True
            else:
                uniq.add(n)

        return False

if __name__ == "__main__":
    s = Solution()
    assert s.containsDuplicate([1,2,3,1]) == True
    assert s.containsDuplicate([1,2,3,4]) == False
    assert s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True



"""
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""