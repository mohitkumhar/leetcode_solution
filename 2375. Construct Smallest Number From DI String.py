class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        result = [(i + 1) for i in range(n + 1)]
        i = 0
        while i < n:
            if pattern[i] == 'D':
                start = i
                while i < n and pattern[i] == 'D':
                    i += 1
                result[start:i + 1] = reversed(result[start:i + 1])
            else:
                i += 1
        result = map(lambda x: str(x), result)

        return ''.join(result)