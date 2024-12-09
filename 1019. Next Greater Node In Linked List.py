# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        def reverse(node):
            prev = None
            current = node

            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            
            return prev

        reverse_head = reverse(head)
        current = reverse_head
        max_stack = []
        result = []

        while current:

            while max_stack and max_stack[-1] <= current.val:
                max_stack.pop()

            result.append(0 if not max_stack else max_stack[-1])

            max_stack.append(current.val)
            current = current.next
        
        result.reverse()
        return result
