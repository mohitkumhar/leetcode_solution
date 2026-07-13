class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        q = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for x in q:
            d = x % 10
            if d < 9:
                q.append(x * 10 + d + 1)

        return [i for i in q if low <= i <= high]
