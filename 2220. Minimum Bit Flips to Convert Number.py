class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:

        xor_representation = start ^ goal

        return bin(xor_representation).count('1')
    