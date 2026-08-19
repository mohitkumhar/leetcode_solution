class Solution:
    def maximumBags(
        self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(rocks)

        differenceArray = []
        count = 0

        for i in range(n):
            differenceArray.append(capacity[i] - rocks[i])

        differenceArray.sort()

        for diff in differenceArray:
            if additionalRocks < diff:
                break
            if diff == 0:
                count += 1
                continue

            additionalRocks -= diff
            count += 1

        return count
