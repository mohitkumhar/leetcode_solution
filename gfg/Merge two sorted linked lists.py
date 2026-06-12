'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

'''
class Solution:
    def sortedMerge(self, head1, head2):
        current1 = head1
        current2 = head2
        ans_node = Node(0)
        dummy_node = ans_node

        while current1 and current2:
            if not current1:
                break
            if not current2:
                break

            if current1.data < current2.data:
                ans_node.next = Node(current1.data)
                ans_node = ans_node.next
                current1 = current1.next
            else:
                ans_node.next = Node(current2.data)
                ans_node = ans_node.next
                current2 = current2.next


        while current1:
            ans_node.next = Node(current1.data)
            ans_node = ans_node.next
            current1 = current1.next

        while current2:
            ans_node.next = Node(current2.data)
            ans_node = ans_node.next
            current2 = current2.next

        return dummy_node.next
