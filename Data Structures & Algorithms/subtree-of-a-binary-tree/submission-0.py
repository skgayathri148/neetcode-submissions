# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        stack = deque([root])
        while stack:
            curr = stack.pop()
            found = self.sameroot(curr, subRoot)
            if found:
                return True
            else:
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
                continue

        return False

    def sameroot(self, p, q):

        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            left = self.sameroot(p.left, q.left)
            right = self.sameroot(p.right, q.right)
            return left and right
        else:
            return False