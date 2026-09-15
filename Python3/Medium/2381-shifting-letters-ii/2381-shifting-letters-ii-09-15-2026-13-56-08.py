class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        events = [0] * n

        for shift in shifts:
            start = shift[0]
            end = shift[1]
            direction = shift[2]

            if direction == 1:
                events[start] += 1
                if end + 1 < n:
                    events[end + 1] -= 1
            else:
                events[start] -= 1
                if end + 1 < n:
                    events[end + 1] += 1

        print(events)
        for i in range(1, len(events)):
            events[i] += events[i - 1]
        print(events)

        s = list(s)
        for i in range(n):
            newChar = chr((ord(s[i]) - ord("a") + events[i]) % 26 + ord("a"))
            s[i] = newChar

        print(s)

        return "".join(s)
