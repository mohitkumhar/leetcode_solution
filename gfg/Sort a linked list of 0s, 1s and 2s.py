'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
	
class Solution:
    def segregate(self, head):
        zeros = 0
        ones = 0
        twos = 0
        
        temp = head
        while temp:
            if temp.data == 0:
                zeros += 1
            elif temp.data == 1:
                ones += 1
            else:
                twos += 1
            
            temp = temp.next
        
        current = head
        while current:
            if zeros > 0:
                current.data = 0
                zeros -= 1
            elif ones > 0:
                current.data = 1
                ones -= 1
            else:
                current.data = 2
                twos -= 1
            current = current.next
        
        return head
    
