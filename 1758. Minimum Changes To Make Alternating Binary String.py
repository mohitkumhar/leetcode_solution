class Solution:
    def minOperations(self, s: str) -> int:
        even_string = '01' * ((len(s) // 2) + 1)
        odd_string = '10' * ((len(s) // 2) + 1)

        count_even = 0
        count_odd = 0

        for i in range(len(s)):
            if s[i] != even_string[i]:
                count_even += 1
            if s[i] != odd_string[i]:
                count_odd += 1

        return min(count_even, count_odd)
