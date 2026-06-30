'''
#LinkedList Node
class LNode:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
#Tree Node        
class TNode:
    def __init__(self, data):
        self.data=data
        self.left = self.right = None
'''

class Solution:
    def sortedListToBST(self, head):
        
        if not head:
            return None

        if not head.next:
            return TNode(head.data)

        # find the middle of the LL
        slow = head
        fast = head
        prev = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        if prev:
            prev.next  = None
        
        # create the BST
        
        root = TNode(slow.data)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
    
        return root
        
        
