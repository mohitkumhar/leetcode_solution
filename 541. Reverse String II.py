class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ''
        turn = True

        for i in range(0, len(s), k):
            min_str = s[i: i+k]

            if turn:
                ans += min_str[::-1]
                turn = False
            elif not turn:
                ans += min_str
                turn = True

        return ans
