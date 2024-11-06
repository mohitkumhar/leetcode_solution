# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        
        def find_mid(node):
            slow = node
            fast = node.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def merge(left, right):

            temp = ListNode(0)
            node = temp
            
            while left and right:
                if left.val < right.val:
                    node.next = left
                    left = left.next
                else:
                    node.next = right
                    right = right.next
                node = node.next

            node.next = left if left else right
            return temp.next

        mid = find_mid(head)
        left = head
        right = mid.next
        mid.next = None

        left = self.sortList(left)

        right = self.sortList(right)

        return merge(left, right)
