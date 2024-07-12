class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def size(self):
        return len(self.items)


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def answer_for_ab(string, x, y):
            stack = Stack()
            score = 0

            for char in string:
                if char == 'b':
                    if not stack.is_empty() and stack.peek() == 'a':
                        score += x
                        stack.pop()
                    else:
                        stack.push(char)
                
                else:
                    stack.push(char)

            remaining = []
            while not stack.is_empty():
                remaining.append(stack.pop())
            remaining.reverse()

            stack = Stack()

            for char in remaining:   # ba
                if char == 'a':
                    if not stack.is_empty() and stack.peek() == 'b':
                        score += y
                        stack.pop()
                    else:
                        stack.push(char)
                else:
                    stack.push(char)
            return score

        def answer_for_ba(string, x, y):
            stack = Stack()
            score = 0

            for char in string:
                if char == 'a':
                    if not stack.is_empty() and stack.peek() == 'b':
                        score += y
                        stack.pop()
                    else:
                        stack.push(char)
                else:
                    stack.push(char)
            remaining = []
            while not stack.is_empty():
                remaining.append(stack.pop())
            remaining.reverse()

            stack = Stack()

            for char in remaining:   # ab
                if char == 'b':
                    if not stack.is_empty() and stack.peek() == 'a':
                        score += x
                        stack.pop()
                    else:
                        stack.push(char)

                else:
                    stack.push(char)
            return score

        
        if x > y:
            return answer_for_ab(s, x, y)
        else:
            return answer_for_ba(s, x, y)

        