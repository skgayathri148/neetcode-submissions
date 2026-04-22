# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        queue = deque([(root, float("-infinity"), float("infinity"))])
        while queue:
            curr, left, right = queue.popleft()
            print("Curr: {}, Left: {}, Right: {}", curr.val, left, right)
            if not (left < curr.val < right):
                return False

            if curr.left:
                print("Left:", curr.left.val)
                queue.append((curr.left, left, curr.val))
                
            if curr.right:
                print("Right:", curr.right.val)
                queue.append((curr.right, curr.val, right))

        return True