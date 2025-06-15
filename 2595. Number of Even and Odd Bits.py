class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = 0
        odd = 0
        n = bin(n)[2:]
        index = 0

        for i in range(len(n) - 1, -1, -1):
            if n[i] == '1':
                if index % 2 == 0:
                    even += 1
                else:
                    odd += 1
            index += 1
        
        return [even, odd]
