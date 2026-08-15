class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def isPossible(day, bloomDay, m, k):
            count = 0
            bouquets = 0

            for bloom in bloomDay:
                if bloom <= day:
                    count += 1

                    if count == k:
                        bouquets += 1
                        count = 0
                else:
                    count = 0

            return bouquets >= m

        if (m * k) > len(bloomDay):
            return -1

        left = min(bloomDay)
        right = max(bloomDay)

        while left < right:
            mid = left + (right - left) // 2

            if isPossible(mid, bloomDay, m, k):
                right = mid
            else:
                left = mid + 1

        return left
