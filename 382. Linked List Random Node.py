# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def traverse(self):
        index = 0
        current = self.head
        while current:
            index += 1
            current = current.next
        
        return index            

    def find_random_node(self, index):
        current = self.head
        temp = 0
        while current and temp != index:
            temp += 1
            current = current.next
        return current

    def getRandom(self) -> int:
        index = self.traverse()

        random_value = random.randint(0, index-1)

        random_node = self.find_random_node(random_value)
    
        return random_node.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()