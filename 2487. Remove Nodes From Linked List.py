# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(node_head):
            prev = None
            current = node_head

            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            return prev
        

        reversed_head = reverse(head)

        max_val = float('-inf')
        
        dummy = ListNode(0)
        new_list_tail = dummy
        current = reversed_head

        while current:
            if current.val >= max_val:
                max_val = current.val
                new_list_tail.next = current
                new_list_tail = new_list_tail.next
            
            current = current.next
        new_list_tail.next = None
        
        head = reverse(dummy.next)
        return head
