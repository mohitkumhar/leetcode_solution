# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        def check(array: List[int], condn: bool) -> bool:
            if condn:
                # for even level
                for i in range(len(array)):
                    if array[i] % 2 == 0:
                        return False
                
                for i in range(1, len(array)):
                    if array[i - 1] >= array[i]:
                        return False
                return True

            else:
                # for odd level
                for i in range(len(array)):
                    if array[i] % 2 == 1:
                        return False

                for i in range(1, len(array)):
                    if array[i - 1] <= array[i]:
                        return False
                return True

        queue = [root]
        condition = True

        while queue:
            temp = []
            level_list = []

            for node in queue:
                level_list.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            if not check(level_list, condition):
                return False

            condition = not condition
            queue = temp

        return True
