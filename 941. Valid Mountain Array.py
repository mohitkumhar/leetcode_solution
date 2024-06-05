class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3:
            return False
        start = 0
        end = len(arr) - 1

        while start + 1 < len(arr) - 1 and arr[start] < arr[start + 1]:
            start += 1

        while end - 1 > 0 and arr[end] < arr[end - 1]:
            end -= 1

        return start == end
