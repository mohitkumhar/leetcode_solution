class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        can_s1_break_s2 = all(a >= b for a, b in zip(s1, s2))
        can_s2_break_s1 = all(a >= b for a, b in zip(s2, s1))

        return can_s1_break_s2 or can_s2_break_s1
