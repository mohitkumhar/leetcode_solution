class Solution:
    def removePalindromeSub(self, s: str) -> int:

        
        s_list = list(s)

        start = 0
        end = len(s) - 1

        while start <= end:
            star = s_list[start]

            s_list[start] = s_list[end]
            s_list[end] = star

            start += 1
            end -= 1

        if ''.join(s_list) == s:
            return 1
        return 2
