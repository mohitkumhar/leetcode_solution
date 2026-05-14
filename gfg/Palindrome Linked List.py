'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def isPalindrome(self, head):
        elements = []
        current = head

        while current:
            elements.append(current.data)
            current = current.next

        return elements == elements[::-1]
