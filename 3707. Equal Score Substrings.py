class Solution:
    def scoreBalance(self, s: str) -> bool:
        def helper(left_str, right_str):
            left_count = 0
            right_count = 0

            for char in left_str:
                temp = ord(char) - 96
                left_count += temp
            for char in right_str:
                temp = ord(char) - 96
                right_count += temp
            return left_count, right_count

        s = list(s)
        for i in range(len(s)-1):
            left, right = helper(s[:i+1], s[i+1:])
            if left == right:
                return True
        return False
