# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge_sort(list1, list2):
            if not list1:
                return list2
            if not list2:
                return list1

            dummy_node = ListNode(0)
            node = dummy_node

            curr1 = list1
            curr2 = list2

            while curr1 and curr2:
                if curr1.val <= curr2.val:
                    node.next = ListNode(curr1.val)
                    node = node.next
                    curr1 = curr1.next

                else:
                    node.next = ListNode(curr2.val)
                    node = node.next
                    curr2 = curr2.next

            while curr1:
                node.next = ListNode(curr1.val)
                node = node.next
                curr1 = curr1.next

            while curr2:
                node.next = ListNode(curr2.val)
                node = node.next
                curr2 = curr2.next

            return dummy_node.next

        n = len(lists)
        result = None
        for i in range(n):
            result = merge_sort(result, lists[i])

        return result
