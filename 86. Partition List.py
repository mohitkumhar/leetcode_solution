# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        left_dummy = ListNode(0)
        right_dummy = ListNode(0)

        left_list = left_dummy

        right_list = right_dummy

        while head:
            if head.val < x:
                left_list.next = head
                left_list = left_list.next
            
            else:
                right_list.next = head
                right_list = right_list.next
            
            head = head.next
        
        left_list.next = right_dummy.next

        right_list.next = None

        return left_dummy.next
        
                                         
        