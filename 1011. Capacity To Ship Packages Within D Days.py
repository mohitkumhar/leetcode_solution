class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int: 
        def check_shipment(ship_weight):
            count = 0
            day = 1
            for weight in weights:
                if count + weight > ship_weight:
                    day += 1
                    count = 0
                count += weight
            return day <= days

        left = max(weights)
        right = sum(weights)
        least_weight = 0

        while left < right:
            mid = (right + left) // 2

            if check_shipment(mid):
                right = mid
            else:
                left = mid + 1

        return right
