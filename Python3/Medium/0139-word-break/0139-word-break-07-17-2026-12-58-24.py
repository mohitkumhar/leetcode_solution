class Solution:
    def __init__(self):
        self.n = 0
        self.memo = []

    def solve(self, start: int, s: str, wordDict: List[str]) -> bool:
        if start == self.n:
            self.memo[start] = 1
            return True
        if self.memo[start] != 0:
            if self.memo[start] == 1:
                return True
            return False

        for end in range(start + 1, self.n + 1):
            if s[start:end] in wordDict and self.solve(end, s, wordDict):
                self.memo[end] = 1
                return True
        self.memo[start] = -1
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        self.n = len(s)
        self.memo = [0] * (self.n + 1)

        return self.solve(0, s, wordDict)
