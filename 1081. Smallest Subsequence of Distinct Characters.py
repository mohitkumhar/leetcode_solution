class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
        freq = {char: 0 for char in s}

        for char in s:
            freq[char] += 1


        stack = []
        visited = set()

        for char in s:
            freq[char] -= 1

            if char in visited:
                continue

            while stack and stack[-1] > char and freq[stack[-1]] > 0:
                visited.remove(stack.pop())

            stack.append(char)
            visited.add(char)
        
        return  ''.join(stack)