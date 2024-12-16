# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validation(root, min_val, max_val):
            if not root:
                return True
            
            if root.val <= min_val or root.val >= max_val:
                return False

            return (
                validation(root.left, min_val, root.val) and 
                validation(root.right, root.val, max_val)
            )

        # return validation(root, -2**31, 2**31 - 1) 이렇게하면 틀리고 아래로하면 맞음. 이해불가
        return validation(root, -inf, inf)
