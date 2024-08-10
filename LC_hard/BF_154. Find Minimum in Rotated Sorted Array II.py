class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = len(nums) - 1
        if l == 0:
            return nums[l]

        mid = l // 2

        left = 0
        left_found = nums[0]
        jack, back = False, False
        while mid - left > 0:

            if nums[mid] < nums[mid - left]:
                left_found = nums[mid - left]
                break

            elif nums[mid] > nums[mid - left] and nums[mid - left - 1] > nums[mid - left]:
                left_found = nums[mid - left]
                break

            elif left == 0 and mid - 1 >= 0 and nums[mid] < nums[mid - 1]:
                jack = True
                left += 1
            elif left != 0 and nums[mid] == nums[mid - left]:
                left_found = min(nums[mid - left], left_found)
                left += 1
            else:
                left += 1

        right = 0
        right_found = nums[-1]
        while mid + right <= l:
            if nums[mid] > nums[mid + right]:
                right_found = nums[mid + right]
                back = False
                break
            elif nums[mid] < nums[mid + right]:
                back = True
                right += 1
            elif nums[mid] == nums[mid + right]:
                right_found = min(nums[mid + right], right_found)
                right += 1
            else:
                right += 1

        if jack and back:
            return nums[mid]

        return min(left_found, right_found)


if __name__ == "__main__":
    s = Solution()
    assert s.findMin([1,3,5]) == 1
    assert s.findMin([2,2,2,0,1]) == 0



"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:
[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.
You must decrease the overall operation steps as much as possible.

 

Example 1:
Input: nums = [1,3,5]
Output: 1

Example 2:
Input: nums = [2,2,2,0,1]
Output: 0
 

Constraints:
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
nums is sorted and rotated between 1 and n times.
"""