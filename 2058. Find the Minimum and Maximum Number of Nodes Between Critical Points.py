# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        current = head.next
        prev = head

        critical_points = []
        index = 1

        while current.next:
            if current.val < prev.val and current.val < current.next.val:
                critical_points.append(index)

            elif current.val > prev.val and current.val > current.next.val:
                critical_points.append(index)

            prev = current
            current = current.next
            index += 1

        if len(critical_points) < 2:
            return [-1, -1]

        max_diff = critical_points[-1] - critical_points[0]

        min_diff = float('inf')

        for i in range(len(critical_points) - 1):
            diff = critical_points[i + 1] - critical_points[i]

            min_diff = min(min_diff, diff)

        return [min_diff, max_diff]
