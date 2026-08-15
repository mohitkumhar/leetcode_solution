class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def isPossible(day):
            count = 0
            currBouquet = 0

            for bloom in bloomDay:
                if bloom <= day:
                    count += 1

                    if count == k:
                        currBouquet += 1
                        count = 0
                else:
                    count = 0

            return currBouquet >= m

        if m * k > len(bloomDay):
            return -1

        left = min(bloomDay)
        right = max(bloomDay)

        while left < right:
            mid = left + (right - left) // 2

            if isPossible(mid):
                right = mid
            else:
                left = mid + 1

        return left
