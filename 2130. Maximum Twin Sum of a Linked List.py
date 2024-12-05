# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        
        max_twin_sum = 0
        first = head
        second = prev

        while first and second:
            max_twin_sum = max(max_twin_sum, first.val + second.val)
            first = first.next
            second = second.next
        
        return max_twin_sum
