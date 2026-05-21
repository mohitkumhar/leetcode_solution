class Solution:
    def isBitSet(self, n):
        binary = bin(n)[2:]
        values = binary.count("1")

        return values == len(binary)
