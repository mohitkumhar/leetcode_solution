class Solution:
    def reverseByType(self, s: str) -> str:
        s = list(s)
        n = len(s)

        i = 0
        j = n - 1

        while i < j:
            while i < j and not s[i].isalpha():
                i += 1

            while i < j and not s[j].isalpha():
                j -= 1

            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        i = 0
        j = n - 1

        while i < j:
            while i < j and s[i].isalpha():
                i += 1

            while i < j and s[j].isalpha():
                j -= 1

            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return "".join(s)
