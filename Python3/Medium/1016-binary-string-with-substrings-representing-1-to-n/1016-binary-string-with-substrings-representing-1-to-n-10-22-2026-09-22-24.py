class Solution:
    def queryString(self, s: str, n: int) -> bool:
        a = bin(n)[2:]

        for i in range(1, n + 1):
            num = bin(i)[2:]
            if num not in s:
                return False

        return True
