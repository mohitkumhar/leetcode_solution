class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [0] * (len(encoded) + 1)
        arr[0] = first

        for i in range(len(encoded)):
            arr[i + 1] =  encoded[i] ^ arr[i]
        return arr
