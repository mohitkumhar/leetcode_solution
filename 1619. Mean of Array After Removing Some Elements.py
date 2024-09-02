class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)

        arr.sort()

        five_per = n // 20

        arr = arr[five_per: n - five_per]

        return sum(arr) / len(arr)
        