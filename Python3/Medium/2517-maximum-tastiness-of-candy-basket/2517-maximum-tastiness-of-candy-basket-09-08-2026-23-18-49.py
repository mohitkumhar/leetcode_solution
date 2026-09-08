class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()

        def isPossible(diff):
            count = 1
            n = len(price)
            last = price[0]

            for i in range(1, n):
                if price[i] - last >= diff:
                    count += 1
                    last = price[i]

                if count >= k:
                    return True
            return False

        left = 0
        right = price[-1] - price[0]

        while left <= right:
            mid = left + (right - left) // 2

            if isPossible(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result
