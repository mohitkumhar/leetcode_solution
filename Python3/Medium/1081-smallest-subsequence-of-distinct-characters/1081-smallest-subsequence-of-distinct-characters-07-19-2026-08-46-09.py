class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1

        stack = []
        seen = set()

        for char in s:
            freq[char] -= 1
            if char in seen:
                continue

            while stack and stack[-1] > char and freq[stack[-1]] > 0:
                seen.remove(stack.pop())

            stack.append(char)
            seen.add(char)

        return "".join(stack)
