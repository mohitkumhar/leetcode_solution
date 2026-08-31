# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        prev = head
        curr = head.next
        index = 1
        criticalPoint = []

        while curr.next:
            if prev.val < curr.val > curr.next.val:
                criticalPoint.append(index)
            elif prev.val > curr.val < curr.next.val:
                criticalPoint.append(index)

            prev = curr
            curr = curr.next
            index += 1

        if len(criticalPoint) < 2:
            return [-1, -1]

        maxVal = criticalPoint[-1] - criticalPoint[0]
        minVal = float("inf")

        for i in range(len(criticalPoint) - 1):
            diff = criticalPoint[i + 1] - criticalPoint[i]

            minVal = min(minVal, diff)

        return [minVal, maxVal]
