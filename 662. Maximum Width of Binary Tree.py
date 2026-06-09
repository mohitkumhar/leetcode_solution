# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_width = 0
        queue = [(root, 0)]

        while queue:
            n = len(queue)
            first_element_idx = queue[0][1]
            last_element_idx = queue[-1][1]
            self.max_width = max(self.max_width, last_element_idx - first_element_idx + 1)

            for _ in range(len(queue)):
                node, idx = queue.pop(0)

                if node.left:
                    queue.append((node.left, 2 * idx + 1))
                if node.right:
                    queue.append((node.right, 2 * idx + 2))

        return self.max_width
