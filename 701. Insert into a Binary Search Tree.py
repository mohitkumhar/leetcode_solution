# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def insert_helper(node):
            if node is None:
                return TreeNode(val)
            
            elif val < node.val:
                node.left = insert_helper(node.left)
            
            elif val > node.val:
                node.right = insert_helper(node.right)
            
            return node
            
            

        return insert_helper(root)
        