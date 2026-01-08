# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        queue = [(root, 1)]

        if depth == 1:
            new_node = TreeNode(val)
            new_node.left = root
            return new_node

        while queue:
            curr, dep = queue.pop(0)

            if dep == depth - 1:
                
                old_left = curr.left
                old_right = curr.right

                new_right = TreeNode(val)
                new_left = TreeNode(val)

                new_right.right = old_right
                new_left.left = old_left

                curr.left = new_left
                curr.right = new_right

            else:
                if curr.left:
                    queue.append((curr.left, dep + 1))
                if curr.right:
                    queue.append((curr.right, dep + 1))

        return root
