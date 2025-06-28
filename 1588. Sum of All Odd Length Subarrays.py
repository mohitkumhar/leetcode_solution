class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        for i in range(len(arr)):
            for j in range(len(arr)):
                if len(arr[i: j + 1]) % 2 == 1:
                    result += sum(arr[i: j + 1])

        return result