class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(i, j, arr):
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        n = len(nums)

        k %= n
        reverse(0, n - 1, nums)
        reverse(0, k - 1, nums)
        reverse(k, n - 1, nums)
