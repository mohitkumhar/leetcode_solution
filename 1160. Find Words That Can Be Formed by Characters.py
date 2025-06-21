class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def check(word):
            word_count = {}
            char_count = {}

            for char in chars:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1

            for char in word:
                if not char in char_count.keys():
                    return 0
                else:
                    if char_count[char] >= 1:
                        char_count[char] -= 1
                    else:
                        return 0
            return len(word)

        count = 0
        for word in words:
            count += check(word)

        return count
