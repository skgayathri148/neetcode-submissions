# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        stack = deque([])
        stack.append(root)
        res = []
        while stack:
            right = None
            for i in range(len(stack)):
                curr = stack.popleft()
                if curr:
                    right = curr
                    stack.append(curr.left)
                    stack.append(curr.right)
            if right:
                res.append(right.val)
        return res