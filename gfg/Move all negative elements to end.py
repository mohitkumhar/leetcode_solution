class Solution:
    def segregateElements(self, arr):
        temp = []

        for num in arr:
            if num >= 0:
                temp.append(num)
        for num in arr:
            if num < 0:
                temp.append(num)

        for i in range(len(arr)):
            arr[i] = temp[i]
