class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        nums = []
        i = 0
        while i < len(word):
            temp = ''
            while i < len(word) and word[i].isnumeric():
                temp += word[i]
                i += 1

            if temp:
                temp = str(temp)
                temp = temp.lstrip('0')
                nums.append(temp)
            i += 1

        return len(set(nums))
