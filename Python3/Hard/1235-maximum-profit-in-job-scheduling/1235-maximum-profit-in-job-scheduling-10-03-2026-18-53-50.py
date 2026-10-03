import gc

class Solution:
    def jobScheduling(
        self, startTime: list[int], endTime: list[int], profit: list[int]
    ) -> int:

        def findNextElement(array, left, endElement):
            right = len(array) - 1
            result = len(array)

            while left <= right:
                mid = left + (right - left) // 2

                if array[mid][0] >= endElement:
                    result = mid
                    right = mid - 1
                else:
                    left = mid + 1

            return result

        def solve(i, array):
            if i >= len(array):
                return 0
            
            if i in memo:
                return memo[i]

            next = findNextElement(array, i + 1, array[i][1])

            take = array[i][2] + solve(next, array)
            notTake = solve(i + 1, array)

            memo[i] = max(take, notTake)

            return memo[i]

        array = []

        for i in range(len(startTime)):
            array.append((startTime[i], endTime[i], profit[i]))

        array.sort()
        memo = {}

        gc.collect()
        return solve(0, array)
