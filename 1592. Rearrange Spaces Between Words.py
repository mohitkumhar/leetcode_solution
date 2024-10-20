class Solution:
    def reorderSpaces(self, text: str) -> str:

        words = text.split()
        words_size = len(words)
        spaces = text.count(' ')

        if words_size == 1:
            return words[0] + (' ' * spaces)


        spaces_between = spaces // (words_size - 1)
        extra_spaces = spaces % (words_size - 1)


        result = (' ' * spaces_between).join(words)
        result += (' ' * extra_spaces)

        return result


        