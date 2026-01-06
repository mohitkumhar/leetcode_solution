# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        stack = [root]
        matrix = {}

        while stack:
            node = stack.pop()

            if node.left:
                if not node.val in matrix:
                    matrix[node.val] = []
                matrix[node.val].append(node.left.val)

                if not node.left.val in matrix:
                    matrix[node.left.val] = []
                matrix[node.left.val].append(node.val)

                stack.append(node.left)

            if node.right:
                if not node.val in matrix:
                    matrix[node.val] = []
                matrix[node.val].append(node.right.val)

                if not node.right.val in matrix:
                    matrix[node.right.val] = []
                matrix[node.right.val].append(node.val)

                stack.append(node.right)

        queue = [(target.val, 0)]
        visited = set()
        visited.add(target.val)
        result = []

        while queue:
            current, distance = queue.pop(0)
            if distance == k:
                result.append(current)

            for neighbour in matrix.get(current, []):
                if not neighbour in visited:
                    queue.append((neighbour, distance + 1))
                    visited.add(neighbour)

        return result
