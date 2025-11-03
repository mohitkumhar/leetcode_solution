class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        counter = set()
        ans = []

        for char in word:
            if char == char.lower():
                if char.lower() not in ans and char.upper() in counter:
                    ans.append(char.lower())
            elif char == char.upper():
                if char.lower() not in ans and char.lower() in counter:
                    ans.append(char.lower())
            counter.add(char)
        return len(ans)
