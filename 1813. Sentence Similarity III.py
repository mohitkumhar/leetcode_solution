class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:

        if len(sentence1.split()) > len(sentence2.split()):
            sentence1, sentence2 = sentence2, sentence1
        
        sentence1 = sentence1.split()
        sentence2 = sentence2.split()
        
        while sentence1 and sentence2 and sentence1[0] == sentence2[0]:
            sentence1.pop(0)
            sentence2.pop(0)
            
        while sentence1 and sentence2 and sentence1[-1] == sentence2[-1]:
            sentence1.pop()
            sentence2.pop()
        
        return not sentence1

