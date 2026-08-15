class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canEat(hr):
            currHours = 0

            for pile in piles:
                currHours += pile // hr

                if pile % hr != 0:
                    currHours += 1

            return currHours <= h

        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right - left) // 2

            if canEat(mid):
                right = mid
            else:
                left = mid + 1

        return left
