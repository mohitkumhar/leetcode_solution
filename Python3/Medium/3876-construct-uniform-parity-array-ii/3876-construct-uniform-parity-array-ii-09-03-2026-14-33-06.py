class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        minOdd = float("inf")
        minEven = float("inf")

        for num in nums1:
            if num % 2 == 0:
                minEven = min(minEven, num)
            else:
                minOdd = min(minOdd, num)

        if minEven == float("inf") or minOdd == float("inf"):
            return True

        return minEven > minOdd
