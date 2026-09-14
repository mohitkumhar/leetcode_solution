class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        events = {}

        for segment in segments:
            events[segment[0]] = events.get(segment[0], 0) + segment[2]
            events[segment[1]] = events.get(segment[1], 0) - segment[2]

        currSum = 0
        start = None

        ans = []

        for key, value in sorted(events.items()):
            if start is not None and currSum > 0:
                ans.append([start, key, currSum])

            currSum += value
            start = key
        return ans
