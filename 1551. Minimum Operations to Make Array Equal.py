class Solution:
    def minOperations(self, n: int) -> int:
        arr = []
        count = 0

        for i in range(n):
            arr.append((2 * i) + 1)
        median = arr[n // 2] if n % 2 == 1 else (arr[n // 2] + arr[n // 2 - 1]) // 2

        for i in range(len(arr) // 2):
            count += abs(arr[i] - median)

        return count
