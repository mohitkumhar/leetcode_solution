class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        events = [0] * (n + 1)

        for booking in bookings:
            start = booking[0]
            end = booking[1]
            passangers = booking[2]

            events[start] += passangers
            if end + 1 <= n:
                events[end + 1] -= passangers

        currSum = 0
        result = []

        for event in events:
            currSum += event
            result.append(currSum)

        return result[1:]
