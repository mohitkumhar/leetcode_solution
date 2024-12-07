# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        first_node = None
        second_node = None

        current = head
        i = 0

        while current:
            i += 1
            if i == k:
                first_node = current
            current = current.next
        
        current = head

        for _ in range(i - k):
            print(current.val)
            current = current.next
        
        second_node = current
    
        if first_node and second_node:
            first_node.val, second_node.val = second_node.val, first_node.val

        return head

        