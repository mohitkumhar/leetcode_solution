class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        def count_char(s):
            count = {}
            for i in s:
                if i.isalpha():
                    i = i.lower()
                    if i not in count:
                        count[i] = 1
                    else:
                        count[i] += 1
            return count

        def help_checker(word, target_count):
            word_count = count_char(word)

            for char in target_count:
                if char not in word_count or word_count[char] < target_count[char]:
                    return False

            return True

        plate_count = count_char(licensePlate)
        shortest_word = None

        for word in words:
            if help_checker(word, plate_count):
                if shortest_word == None or len(word) < len(shortest_word):
                    shortest_word = word
        return shortest_word
