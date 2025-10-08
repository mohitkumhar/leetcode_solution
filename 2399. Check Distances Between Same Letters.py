class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        arr = [-1] * 26
        for i, char in enumerate(s):
            index = ord(char) - 97
            if arr[index] == -1:
                arr[index] = i
            else:
                if i - arr[index] - 1 != distance[index]:
                    return False
        return True
