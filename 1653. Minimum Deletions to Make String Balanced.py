class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack = []
        deletion = 0

        for char in s:
            if char == 'b':
                stack.append(char)

            else:
                if stack:
                    stack.pop()
                    deletion+=1

        return deletion
