class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        def check_prefix(word, searchWord):
            return word[:len(searchWord)] == searchWord
            


        index = 0
        sentence = sentence.split()
        inside = False

        for sent in sentence:
            print("index: ", index, "sentence: ", sent)
            index += 1
            if searchWord in sent:
                if check_prefix(sent, searchWord):
                    inside = True
                    break

        if inside:
            return index
        else:
            return -1
