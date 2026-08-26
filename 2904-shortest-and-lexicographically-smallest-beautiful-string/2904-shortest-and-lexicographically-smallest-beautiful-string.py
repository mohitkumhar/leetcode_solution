class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)

        ans = None

        ones = 0
        left = 0

        for right in range(n):

            if s[right] == "1":
                ones += 1

            while ones > k:
                if s[left] == "1":
                    ones -= 1
                left += 1

            if ones == k:

                while left <= right and s[left] == "0":
                    left += 1

                curr = s[left : right + 1]

                if (
                    not ans
                    or len(curr) < len(ans)
                    or (len(curr) == len(ans) and curr < ans)
                ):
                    ans = curr

        return ans if ans is not None else ""
