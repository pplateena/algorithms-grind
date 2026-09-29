class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        answer = set()

        i = 0
        l = len(nums)
        # i != j and i != k
        while i < l:

            # target = 0 - nums[i]
            j = i + 1
            print(j)
            while j < l:
                target = 0 - nums[i] - nums[j]
                print(j, 'j')
                if target in nums[j + 1:]:
                    k = nums[j + 1:].index(target) + j
                    answer.add((i, j, k))
                    k += 1
                    while k < l:
                        print(k, 'k')
                        if target in nums[k:]:
                            answer.add((i, j, nums[k:].index(target)))
                            k = nums[k:].index(target) + 1
                        else:
                            break
                j += 1

            i += 1

        return [list(n) for n in answer]

if __name__ == "__main__":
    s = Solution()
    ## requires to implent tree builder
    assert s.threeSum([-1,0,1,2,-1,-4]) == "sad"
    # assert s.groupAnagrams([""]) == [[""]]
    # assert s.groupAnagrams(["a"]) == [["a"]]

"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""
