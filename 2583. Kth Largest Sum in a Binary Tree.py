# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue = [root]
        level_sum = []

        while queue:
            temp = []
            temp_level_sum = []

            for node in queue:
                temp_level_sum.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            level_sum.append(sum(temp_level_sum))
            queue = temp

        # print(level_sum)
        # print(sorted(level_sum))
        # print(sorted(level_sum, reverse=True))

        if len(level_sum) <= k - 1:
            return -1

        return sorted(level_sum, reverse=True)[k - 1]