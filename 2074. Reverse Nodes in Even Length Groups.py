# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        current = head

        group_size = 1

        while current:
            group = []

            for _ in range(group_size):
                if not current:
                    break
                group.append(current)
                current = current.next
            
            if len(group) % 2 == 0:
                group.reverse()
            
            for node in group:
                prev.next = node
                prev = node
            
            group_size += 1
        
        prev.next = None

        return dummy.next
