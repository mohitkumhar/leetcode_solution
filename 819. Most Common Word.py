class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        normal_str = ""

        for char in paragraph:
            if char.isalnum():
                normal_str += char.lower()

            else:
                normal_str += " "

        words = normal_str.split()

        result = {}

        for word in words:
            if word not in banned:
                if word not in result:
                    result[word] = 1

                else:
                    result[word] += 1

        max_value = 0
        ans = ""

        for key, value in result.items():
            if value > max_value:
                max_value = value
                ans = key

        return ans
