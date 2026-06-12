# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        matrix = {}

        def solve(node):
            if not node:
                return None

            left_node = solve(node.left)
            right_node = solve(node.right)

            if node.val not in matrix:
                matrix[node.val] = []
            if left_node:
                matrix[node.val].append(left_node.val)
                matrix[left_node.val].append(node.val)
            if right_node:
                matrix[node.val].append(right_node.val)
                matrix[right_node.val].append(node.val)

            return node
        solve(root)

        queue = [start]
        visited = {start}
        dist = -1

        while queue:
            n = len(queue)

            for _ in range(n):
                node = queue.pop(0)

                for nei in matrix[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)

            dist += 1

        return dist
