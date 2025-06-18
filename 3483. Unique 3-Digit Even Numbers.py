class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        result = set()
        n = len(digits)

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and i != k and j != k:
                        if digits[i] != 0:
                            if digits[k] % 2 == 0:
                                result.add(digits[i] * 100 + digits[j] * 10 + digits[k])
        return len(result)
