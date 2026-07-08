class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        ans = []
        MOD = 10**9 + 7
        n = len(s)
        prefix_sum = [0] * (n + 1)
        digit_up_to = [0] * (n + 1)
        power_of_10 = [1] * (n + 1)
        non_zero = [0] * (n + 1)

        for i, char in enumerate(s):
            prefix_sum[i + 1] = (prefix_sum[i] + int(char)) % MOD
            power_of_10[i + 1] = (power_of_10[i] * 10) % MOD

            non_zero[i + 1] = non_zero[i]

            if char != "0":
                non_zero[i + 1] += 1
                digit_up_to[i + 1] = (digit_up_to[i] * 10 + int(char)) % MOD
            else:
                digit_up_to[i + 1] = digit_up_to[i]

        for left, right in queries:
            curr_sum = prefix_sum[right + 1] - prefix_sum[left]
            curr_str1 = digit_up_to[right + 1]
            curr_str2 = digit_up_to[left]

            diff_len = non_zero[right + 1] - non_zero[left]

            curr_str2 = (curr_str2 * power_of_10[diff_len]) % MOD

            curr_str = curr_str1 - curr_str2
            ans.append((curr_str * curr_sum) % MOD)

        return ans
