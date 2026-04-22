# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        curr = root

        while curr:
            if not curr.left:
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right
            else:
                pre = curr.left
                while pre.right and pre.right != curr:
                    pre = pre.right
                
                if not pre.right:
                    pre.right = curr
                    curr = curr.left
                else:
                    pre.right = None
                    k -= 1
                    if k == 0:
                        return curr.val
                    curr = curr.right
        
        return -1
