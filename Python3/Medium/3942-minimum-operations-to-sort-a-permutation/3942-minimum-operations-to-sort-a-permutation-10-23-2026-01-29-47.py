class Solution:
    def minOperations(self, A: List[int]) -> int:
        n = len(A)
        asc = dsc = 1

        for i in range(1, n):
            asc += A[i] == (A[i - 1] + 1) % n
            dsc += A[i - 1] == (A[i] + 1) % n

        if asc == n:
            return 0 if not A[0] else min(n - A[0], A[0] + 2)

        if dsc == n:
            return min(n - A[-1], A[-1]) + 1

        return -1