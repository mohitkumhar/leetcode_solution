class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        ans = float('inf')
        for i in range(n):
            if words[i] == target:
                dist = abs(i - startIndex)
                ans = min(ans, dist, n - dist)

        return ans if ans != float('inf') else -1
