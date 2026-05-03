class Solution:
    def getMinMax(self, arr):
        maximum = 0
        minimum = float('inf')

        for num in arr:
            if num > maximum:
                maximum = num
            if num < minimum:
                minimum = num

        return [minimum, maximum]
