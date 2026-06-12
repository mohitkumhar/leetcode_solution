'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def distCandy(self, root):
        self.total_moves = 0

        def solve(node):
            if not node:
                return 0

            left_candie = solve(node.left)
            right_candie = solve(node.right)

            self.total_moves += abs(left_candie) + abs(right_candie)

            return (left_candie + right_candie + node.data) - 1

        solve(root)
        return self.total_moves
