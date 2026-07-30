class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        def backtrack(i, currComb, prev):
            if len(currComb) == n:
                result.append("".join(currComb))
                return

            for j in range(3):
                if prev == -1 or prev != s[j]:
                    currComb.append(s[j])
                    temp = prev
                    prev = s[j]

                    backtrack(j + 1, currComb, prev)

                    currComb.pop()
                    prev = temp

        result = []
        s = ["a", "b", "c"]

        backtrack(0, [], -1)
        if (k - 1) >= len(result):
            return ""
        return result[k - 1]
