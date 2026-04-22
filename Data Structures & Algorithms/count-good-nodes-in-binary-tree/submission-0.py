# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        queue = deque([])
        queue.append((root, -float('infinity')))

        while queue:
            curr, max_val = queue.popleft()
            if curr.val >= max_val:
                count += 1
            
            if curr.left:
                queue.append((curr.left, max(max_val, curr.val)))
            if curr.right:
                queue.append((curr.right, max(max_val, curr.val)))

        return count