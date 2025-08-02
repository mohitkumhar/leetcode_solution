class Solution:
    def capitalizeTitle(self, title: str) -> str:
        result = []

        for word in title.split():
            if len(word) > 2:
                result.append(word.capitalize())
            else:
                result.append(word.lower())
        return ' '.join(result)
