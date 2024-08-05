class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        n = len(nums)
        """
        in order to come closer to O(n) and create working byproduct
        we need to operate on normal and reversed list simultaneously 
        """
        left_part = [1] * n
        right_part = [1] * n

        # we don't have any elements left of first, so range(1, len(nums))
        for i in range(1, n):
            left_part[i] = left_part[i - 1] * nums[i - 1]
        """
        to form full product of array we would have to perform left[i] * right[i]
        inside the range we exclude last element, setting starting point to the last element
        and reverse the range for the right part
        """
        for i in range(n - 2, -1, -1):
            right_part[i] = right_part[i + 1] * nums[i + 1]

        # now we construct final products
        return [right_part[i] * left_part[i] for i in range(n)]


if __name__ == "__main__":
    s = Solution()
    assert s.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
