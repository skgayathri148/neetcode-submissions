# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = root.val

        def dfs_sum(node):
            nonlocal max_sum
            if not node:
                return 0
            left_sum = dfs_sum(node.left)
            right_sum = dfs_sum(node.right)
            left_sum = max(left_sum, 0)
            right_sum = max(right_sum, 0)
            max_sum = max(max_sum, left_sum + node.val + right_sum)
            return node.val + max(left_sum, right_sum)

        dfs_sum(root)
        return max_sum