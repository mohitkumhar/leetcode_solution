class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:

        start = 0
        end = k
        ans = 0

        num_str = str(num)

        while end <= len(num_str):
            substring = num_str[start : end]
            
            divisor = int(substring)
            print(divisor)

            if divisor != 0 and num % divisor == 0:
                ans += 1

            start += 1
            end += 1
        
        return ans