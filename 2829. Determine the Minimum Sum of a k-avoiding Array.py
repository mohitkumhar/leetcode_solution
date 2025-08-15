class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        def check(arr, num):
            for i in arr:
                if i + num == k:
                    return False
            return True

        arr = []
        i = 1
        while len(arr) < n:
            if check(arr, i):
                arr.append(i)
            i += 1

        return sum(arr)