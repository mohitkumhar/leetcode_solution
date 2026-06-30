class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        map = {}
        left = 0
        right = 0

        for right in range(n):
            map[s[right]] = map.get(s[right], 0) + 1

            while len(map) == 3:
                ans += (n - right)

                map[s[left]] -= 1
                if map[s[left]] == 0:
                    del map[s[left]]

                left += 1

        return ans
