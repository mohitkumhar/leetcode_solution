class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        prev = 0

        for b in bank:
            count = b.count("1")

            if count == 0:
                continue

            ans += prev * count
            prev = count

        return ans
