# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        stack = []

        new_root = TreeNode()
        current = new_root

        while stack or root:

            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()

            root.left = None
            current.right = root
            current = root
        
            root = root.right


        return new_root.right