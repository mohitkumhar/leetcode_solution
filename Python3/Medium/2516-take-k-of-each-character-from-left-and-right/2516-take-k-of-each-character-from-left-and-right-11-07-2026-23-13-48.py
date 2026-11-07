class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)

        a_count = s.count("a")
        b_count = s.count("b")
        c_count = s.count("c")

        if a_count < k or b_count < k or c_count < k:
            return -1

        i = 0
        j = 0
        result = 0

        while j < n:
            if s[j] == "a":
                a_count -= 1
            elif s[j] == "b":
                b_count -= 1
            elif s[j] == "c":
                c_count -= 1

            while i <= j and (a_count < k or b_count < k or c_count < k):
                if s[i] == "a":
                    a_count += 1
                elif s[i] == "b":
                    b_count += 1
                elif s[i] == "c":
                    c_count += 1
                i += 1

            result = max(result, j - i + 1)
            j += 1

        return n - result
