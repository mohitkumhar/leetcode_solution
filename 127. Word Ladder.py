class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_count = 1
        wordList = set(wordList)
        queue = [beginWord]

        while queue:
            for i in range(len(queue)):
                word = queue.pop(0)
                if word == endWord:
                    return word_count

                word_array = list(word)

                for i in range(len(word_array)):
                    for j in range(97, 123):

                        char = chr(j)

                        temp_array = list(word_array)
                        temp_array[i] = char

                        if ''.join(temp_array) in wordList: 
                            wordList.remove(''.join(temp_array))
                            queue.append(''.join(temp_array))
            word_count += 1

        return 0
