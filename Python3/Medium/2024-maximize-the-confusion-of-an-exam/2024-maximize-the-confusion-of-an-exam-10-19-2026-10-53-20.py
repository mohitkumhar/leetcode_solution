class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        n = len(answerKey)
        ans = 0

        # make everyone T
        def helper(char):
            i = 0
            j = 0

            flip = 0
            ans = 0

            while j < n:
                if answerKey[j] == char:
                    flip += 1

                while flip > k:
                    if answerKey[i] == char:
                        flip -= 1
                    i += 1
                j += 1

                ans = max(ans, j - i)

            return ans

        return max(helper('F'), helper('T'))