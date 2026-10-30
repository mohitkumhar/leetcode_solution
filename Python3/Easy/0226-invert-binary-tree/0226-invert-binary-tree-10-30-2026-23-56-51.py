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

            for _ in range(len(queue)):
                node = queue.pop(0)

                leftVal = None
                rightVal = None

                if node.left:
                    queue.append(node.left)
                    leftVal = node.left

                if node.right:
                    rightVal = node.right
                    queue.append(node.right)

                node.right = leftVal
                node.left = rightVal

        return root
