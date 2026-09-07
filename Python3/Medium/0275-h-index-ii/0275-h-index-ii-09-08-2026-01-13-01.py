class Solution:
    def hIndex(self, citations: List[int]) -> int:

        def isPossible(maxVal):
            count = 0
            for num in citations:
                if num >= maxVal:
                    count += 1

                if count >= maxVal:
                    return True
            return False

        left = 1
        right = max(citations)
        result = 0

        while left <= right:
            mid = left + (right - left) // 2

            if isPossible(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result
