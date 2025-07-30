class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def to_str(x):
            return ''.join(sorted(str(x)))

        target = to_str(n)
        for i in range(30):
            if to_str(1 << i) == target:
                return True
        return False
