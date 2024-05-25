class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        check_list = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
                      "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        ans = []

        for word in words:
            string = ''
            for i in word:

                string += check_list[ord(i)-96-1]

            if string not in ans:
                ans.append(string)
            print(ans)

        return len(ans)
