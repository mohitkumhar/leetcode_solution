# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head.next

        temp = node

        while temp != None:
            sum = 0
            while temp.val != 0:
                sum += temp.val
                temp = temp.next

            node.val = sum

            temp = temp.next

            node.next = temp

            node = temp
        return head.next
