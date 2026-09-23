# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepthRecursive(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if not root:
            return 0

        left_depth = self.maxDepthRecursive(root.left)
        right_depth = self.maxDepthRecursive(root.right)


        return 1 + max(left_depth, right_depth)

    def maxDepthDeque(self, root):
        from collections import deque

        if not root:
            return 0

        max_depth = 1
        dq = deque([(root, max_depth)])

        while dq:
            for _ in range(len(dq)):
                node, depth = dq.popleft()
                if node.left:
                    deque.append((node.left, depth +1))
                if node.right:
                    deque.append((node.right, depth +1))
            max_depth = max(max_depth, depth) # we don't need to recalculate inside for loop, because depth increment is passed in tuples
        return max_depth
if __name__ == "__main__":

    s = Solution()
    # tree builder required to assert
    # assert s.longestConsecutive([100,4,200,1,3,2]) == 4
    # assert s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9

"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""
