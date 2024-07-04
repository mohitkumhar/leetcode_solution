# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:

        current = head

        count = 0
        while current:
            if current.val in nums:
                while current and current.val in nums:
                    current = current.next
                count += 1

            else:
                current = current.next

        return count
