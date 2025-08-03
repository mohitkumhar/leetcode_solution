class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        total = sum(apple)
        res = 0
        for cap in capacity:
            total -= cap
            res += 1
            if total <= 0:
                break
        return res
