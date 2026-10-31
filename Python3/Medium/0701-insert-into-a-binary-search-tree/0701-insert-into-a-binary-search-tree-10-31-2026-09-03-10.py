# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:

        def helper(node, key):
            if not node:
                return TreeNode(key)

            if key < node.val:
                node.left = helper(node.left, key)

            if key > node.val:
                node.right = helper(node.right, key)

            return node

        return helper(root, val)
