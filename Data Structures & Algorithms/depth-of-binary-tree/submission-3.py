# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        if root:
            q.append((root, 1))
        res = 0

        while q:
            node, depth = q.popleft()
            if node:
                res = max(res, depth)
                q.append((node.left, depth + 1))
                q.append((node.right, depth + 1))
        
        return res