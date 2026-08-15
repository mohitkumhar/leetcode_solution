class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2

            missing = arr[mid] - (mid + 1)

            if missing >= k:
                right = mid - 1
            else:
                left = mid + 1

        return left + k
