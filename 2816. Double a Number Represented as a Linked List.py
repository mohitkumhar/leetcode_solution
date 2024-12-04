# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(node_head):
            prev = None
            current = node_head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev
        
        head = reverse(head)
    
        carry = 0
        prev = None
        current = head
        
        while current:
            sum_val = current.val * 2 + carry
            current.val = sum_val % 10
            carry = sum_val // 10
            prev = current
            current = current.next

        if carry:
            prev.next = ListNode(carry)

        return reverse(head)
