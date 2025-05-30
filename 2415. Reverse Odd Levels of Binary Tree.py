# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = [root]
        level = 0

        while queue:
            next_level = []
            for node in queue:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            if level % 2 == 1:
                i = 0
                j = len(queue) - 1
                
                while i < j:
                    queue[i].val, queue[j].val = queue[j].val, queue[i].val
                    i += 1
                    j -= 1
            queue = next_level
            level += 1

        return root
