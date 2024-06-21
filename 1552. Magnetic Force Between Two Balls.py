class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """

        def is_possible(min_dist):
            count = 1
            last_position = position[0]

            for i in range(1, len(position)):
                if position[i] - last_position >= min_dist:
                    count += 1
                    last_position = position[i]

                if count == m:
                    return True
            return False

        position.sort()
        low = 1
        high = position[-1] - position[0]

        best = 0

        while low <= high:
            mid = low + (high - low) // 2

            if is_possible(mid):
                best = mid
                low = mid + 1

            else:
                high = mid - 1

        return best
