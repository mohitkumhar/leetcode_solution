class Solution:
    def minBishopMoves(self, source: list[int], target: list[int]) -> int:

        sr, sc = source
        tr, tc = target

        if (sr + sc) % 2 != (tr + tc) % 2:
            return -1

        if sr - sc == tr - tc or sr + sc == tr + tc:
            return 1

        return 2

        