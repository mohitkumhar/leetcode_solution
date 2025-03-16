class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        def can_repair(mid):
            cars_repaired = 0

            for rank in ranks:
                cars_repaired += int(math.sqrt(mid // rank))

                if cars_repaired >= cars:
                    return True
            return cars_repaired >= cars
        

        left = 1
        right = max(ranks) * cars * cars

        while left < right:
            mid = (left + right) // 2

            if can_repair(mid):
                right = mid
            else:
                left = mid + 1
        return left
