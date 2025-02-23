class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:

        i = 0
        part_len = len(part)
        stack = []

        for char in s:
            stack.append(char)

            if len(stack) >= part_len and ''.join(stack[-part_len:]) == part:
                for _ in range(part_len):
                    stack.pop()

        return ''.join(stack)