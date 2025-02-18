class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        stack = []

        for val in pushed:
            while stack and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)

            stack.append(val)

        while stack and stack[-1] == popped[0]:
            stack.pop()
            popped.pop(0)
            
        return len(stack) == 0
