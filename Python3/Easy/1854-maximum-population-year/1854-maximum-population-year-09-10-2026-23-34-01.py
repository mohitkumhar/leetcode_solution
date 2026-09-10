class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        events = []

        for log in logs:
            events.append((log[0], 1))
            events.append((log[1], -1))

        maxCount = 0
        currCount = 0
        ans = 0

        events.sort()
        for event in events:
            currCount += event[1]

            if currCount > maxCount:
                maxCount = currCount
                ans = event[0]

        return ans
