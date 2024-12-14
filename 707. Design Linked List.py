class MyLinkedList:

    def __init__(self):
        self.head = None


    def get(self, index: int) -> int:
        ind = 0
        current = self.head
        while current:
            if ind == index:
                return current.val
            current = current.next
            ind += 1
        
        return -1
        

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)

        new_node.next = self.head
        self.head = new_node
        

    def addAtTail(self, val: int) -> None:

        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next
        current.next = new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:  # Special case: Add at head
            self.addAtHead(val)
            return

        ind = 0
        dummy = ListNode(val)
        current = self.head

        while current:
            if (ind) == (index - 1):
                dummy.next = current.next
                current.next = dummy
                return
            
            current = current.next
            ind += 1
                

    def deleteAtIndex(self, index: int) -> None:
        if index == 0 and self.head:  # Special case: Delete head
            self.head = self.head.next
            return

        ind = 0

        current = self.head

        while current and current.next:
            if (index - 1) == ind:
                current.next = current.next.next
                return
        
            current = current.next
            ind += 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)