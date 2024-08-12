class Solution:
    def maxArea(self, height: list[int]) -> int:

        first, last = 0, len(height) - 1
        biggest_found = 0

        while first < last:

            side_height = min(height[first], height[last])
            bottom_length = last - first

            can_store = side_height * bottom_length
            biggest_found = max(biggest_found, can_store)

            if side_height == height[first]:
                first += 1
            else:
                last -= 1

        return biggest_found


if __name__ == "__main__":
    s = Solution()
    assert s.maxArea([1,8,6,2,5,4,8,3,7]) == 49
    assert s.maxArea([1,1]) == 1
    assert s.maxArea([150,50,6,2,5,4,3000,200,100]) == 1050

"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the 
ith line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis form a container, such that the 
container contains the most water. Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water 
(blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""