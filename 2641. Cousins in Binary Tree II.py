# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level_sum = []
        queue = [root]

        while queue:
            n = len(queue)
            temp = 0

            for _ in range(n):
                node = queue.pop(0)

                temp += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level_sum.append(temp)

        def dfs(node, depth):
            if not node:
                return None

            sibling_sum = 0
            if node.left:
                sibling_sum += node.left.val
            if node.right:
                sibling_sum += node.right.val

            if node.left or node.right:
                next_level = depth + 1
                next_level_value = level_sum[next_level] - sibling_sum

                if node.left:
                    node.left.val = next_level_value
                if node.right:
                    node.right.val = next_level_value

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        root.val = 0
        dfs(root, 0)

        return root
