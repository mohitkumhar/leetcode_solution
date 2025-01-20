# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        stack = [root]

        for value in preorder[1:]:
            node = None
            child = TreeNode(value)

            while stack and stack[-1].val < value:
                node = stack.pop()

            if node:
                node.right = child
            
            else:
                stack[-1].left = child
        
            stack.append(child)

        return root
