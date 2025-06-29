# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None
        self.first = None
        self.second = None

        def inOrder(node):
            if not node:
                return None

            inOrder(node.left)

            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                    self.second = node
                else:
                    self.second = node
            self.prev = node

            inOrder(node.right)

        inOrder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
