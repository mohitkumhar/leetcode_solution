# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:

        def pre_order_traversal(node, values):
            if node is None:
                return None
            
            values.append(node.val)
            pre_order_traversal(node.left, values)
            pre_order_traversal(node.right, values)
            
        


        values = []
        pre_order_traversal(root, values)

        if len(set(values)) > 1:
            return False

        return True

        