class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        i = 0
        j = n - 1
        s = list(s)

        if s[i] != s[j]:
            return len(s)

        while i < j: 

            if s[i] == s[j]:
                # check prefix
                while i < j and s[i] == s[i + 1]:
                    s[i] = " "
                    i += 1

                # check suffix
                while i < j and s[j] == s[j - 1]:
                    s[j] = " "
                    j -= 1

                s[i] = " "
                s[j] = " "
                i += 1
                j -= 1

            else:
                return len(''.join(s).strip())

        return len(''.join(s).strip())
