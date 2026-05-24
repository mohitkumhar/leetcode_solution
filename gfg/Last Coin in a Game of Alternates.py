class Solution:
    def coin(self, arr):
        n = len(arr)
        i = 0
        j = n - 1

        while i < j:
            if arr[i] > arr[j]:
                arr[i] = -1
                i += 1
            else:
                arr[j] = -1
                j -= 1

        return arr[i]
