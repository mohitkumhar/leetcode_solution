# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        def get_length(node):
            length = 0
            while node:
                node = node.next
                length += 1
            return length

        len1 = get_length(headA)
        len2 = get_length(headB)

        while len1 > len2:
            headA = headA.next
            len1 -= 1

        while len2 > len1:
            headB = headB.next
            len2 -= 1

        while headA and headB:
            if headA == headB:
                return headA

            headA = headA.next
            headB = headB.next

        return None
