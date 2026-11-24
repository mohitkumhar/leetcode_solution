# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None

        queue = [root]

        while queue:
            node = queue.pop(0)

            node.right, node.left = node.left, node.right

            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

        return root
