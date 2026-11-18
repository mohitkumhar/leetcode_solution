class Solution:
    def minChanges(self, s: str) -> int:

        changes = 0

        count = 0
        char = s[0]

        for i in range(len(s)):
            if s[i] == char:
                count += 1
                continue

            if count % 2 == 0:
                count = 1

            else:
                changes += 1
                count = 0

            char = s[i]

        return changes
