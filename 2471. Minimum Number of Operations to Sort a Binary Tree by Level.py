# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def min_swap(arr):
            n = len(arr)
            sorted_arr = sorted([val, i] for i, val in enumerate(arr))
            visited = [False] * n
            swaps = 0

            for i in range(n):
                if visited[i] or i == sorted_arr[i][1]:
                    continue
                
                cycle_len = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = sorted_arr[j][1]
                    cycle_len += 1

                swaps += cycle_len - 1
            return swaps 

        queue = [root]
        result = 0
        while queue:
            temp = []
            level_list = []

            for node in queue:
                level_list.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            
            result += min_swap(level_list)
            queue = temp
        return result