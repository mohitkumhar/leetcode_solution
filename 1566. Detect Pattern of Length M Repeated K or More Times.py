class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)

        for i in range(n - m + 1):
            count = 0

            for j in range(i + m, n, m):
                
                if arr[i: i + m] == arr[j: j + m]:
                    count += 1
                else:
                    break
                
                if count == k - 1:
                    return True

        return False
