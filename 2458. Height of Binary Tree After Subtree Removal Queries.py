# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        self.n = 0
        def total_nodes(node):
            if not node:
                return 0

            self.n += 1
            total_nodes(node.left)
            total_nodes(node.right)

        total_nodes(root)

        nodes_height = [-1] * (self.n + 1)
        level_max_height = [0] * (self.n + 1)
        level_second_max_height = [0] * (self.n + 1)

        def find_height(node, level):
            if not node:
                return 0

            left_max_height = find_height(node.left, level + 1)
            right_max_height = find_height(node.right, level + 1)

            max_height = max(left_max_height, right_max_height) + 1

            if level_max_height[level] < max_height:
                level_second_max_height[level] = level_max_height[level]
                level_max_height[level] = max_height
            elif level_second_max_height[level] < max_height:
                level_second_max_height[level] = max_height

            nodes_height[node.val] = max_height

            return max_height
        find_height(root, 0)

        nodes_level = [-1] * (self.n + 1)
        queue = [(root, 0)]

        while queue:
            size = len(queue)

            for _ in range(size):
                node, level = queue.pop(0)
                nodes_level[node.val] = level

                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))

        result = []
        for query in queries:
            level = nodes_level[query]
            height = nodes_height[query]

            if height == level_max_height[level]:
                height = level_second_max_height[level]
            else:
                height = level_max_height[level]

            result.append(level + height - 1)

        return result
