class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        def can_make_bouquets(day):
            bouquets = 0
            count = 0

            for bloom in bloomDay:
                if bloom <= day:
                    count += 1
                    if count == k:
                        bouquets += 1
                        count = 0

                else:
                    count = 0

            return bouquets >= m

        if m * k > len(bloomDay):
            return -1

        left, right = min(bloomDay), max(bloomDay)

        while left < right:
            mid = left + (right - left) // 2

            if can_make_bouquets(mid):
                right = mid

            else:
                left = mid + 1

        return left
