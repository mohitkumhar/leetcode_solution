class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()

        check = abs(arr[0] - arr[1])

        start = 0
        end = len(arr) - 1

        
        for i in range(1, len(arr)):
            if not abs(arr[i - 1] - arr[i]) == check:
                return False
        return True

        