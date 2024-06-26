# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode()
        ptr = result
        carry = 0

        while l1 != None or l2 != None:
            sum = 0 + carry

            if l1 != None:
                sum += l1.val
                l1 = l1.next

            if l2 != None:
                sum += l2.val
                l2 = l2.next

            carry = sum // 10
            sum = sum % 10
            ptr.next = ListNode(sum)
            ptr = ptr.next

        if carry == 1:
            ptr.next = ListNode(1)
        return result.next
