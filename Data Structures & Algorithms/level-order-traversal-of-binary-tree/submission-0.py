# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = deque([])
        stack.append(root)
        result = []
        while stack:
            res = []
            for i in range(len(stack)):          
                curr = stack.popleft()
                if curr:
                    res.append(curr.val)
                    stack.append(curr.left)
                    stack.append(curr.right)
            if res:
                result.append(res)
                
        return result