class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def isPossible(maxWeight, weights, days):
            currDays = 1
            currWeight = 0

            for weight in weights:
                if (currWeight + weight) > maxWeight:
                    currDays += 1
                    currWeight = weight
                else:
                    currWeight += weight

            return currDays <= days

        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = left + (right - left) // 2

            if isPossible(mid, weights, days):
                right = mid
            else:
                left = mid + 1

        return left