# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def inorder_traversal(node, result):
            if node:
                inorder_traversal(node.left, result)
                result.append(node.val)
                inorder_traversal(node.right, result)

        
        result = []
        inorder_traversal(root, result)
        
        sum = 0
        print(type(result))

        for i in range(len(result)):
            if result[i] >= low and result[i] <= high:
                sum += result[i]
        
        return sum