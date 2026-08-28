# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:

        def findLength(head):
            length = 0
            while head:
                head = head.next
                length += 1
            return length

        curr1 = headA
        curr2 = headB

        len1 = findLength(headA)
        len2 = findLength(headB)

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
