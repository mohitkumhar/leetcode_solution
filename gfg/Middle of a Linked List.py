'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''

class Solution:
    def getMiddle(self, head):
        if not head:
            return None

        current = head

        slow = current.next
        fast = current.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data
