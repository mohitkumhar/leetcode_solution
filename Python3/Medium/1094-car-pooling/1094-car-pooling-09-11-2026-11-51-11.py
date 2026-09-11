class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []

        for trip in trips:
            events.append((trip[1], trip[0]))
            events.append((trip[2], -trip[0]))

        events.sort()
        count = 0

        for event in events:
            count += event[1]

            if count > capacity:
                return False
        return True
