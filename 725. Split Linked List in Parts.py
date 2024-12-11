# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        

        def total_nodes(node_head):
            current = node_head
            sum = 0
            while current:
                current = current.next
                sum += 1

            return sum
        
        total_nodes = total_nodes(head)
        parts = total_nodes // k
        extra = total_nodes % k

        result = []
        current = head

        for i in range(k):
            part_size = parts
            
            if extra > 0:
                part_size += 1
                extra -= 1

            dummy = ListNode(0)
            write = dummy
            for _ in range(part_size):
                if current:
                    write.next = ListNode(current.val)
                    write = write.next
                    current = current.next
                
            result.append(dummy.next)
        
        return result
