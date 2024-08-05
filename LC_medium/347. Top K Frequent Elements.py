class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        nums_dict = dict()

        for number in nums:

            if number in nums_dict.keys():
                nums_dict[number] += 1
            else:
                nums_dict[number] = 1

        sorted_dict = sorted(nums_dict.items(), key=lambda x: x[1])


        return_list = []
        for n in range(k):
            n *= -1
            n -= 1

            return_list.append(sorted_dict[n][0])

        return return_list


if __name__ == "__main__":
    s = Solution()
    assert s.topKFrequent(nums = [1,1,1,2,2,3], k = 2) == [1,2]
    assert s.topKFrequent(nums = [1], k = 1) == [1]


"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""