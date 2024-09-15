# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        def traversal(node, values):
            while node is not None:
                values.append(node.val)
                node = node.next

        

        linked_value = []

        traversal(head, linked_value)

        linked_value = "".join(map(str, linked_value)) 

        return int(linked_value, 2)
