class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:

        def is_prefix(word, string):
            n = len(word)


            if word in string[:n]:
                return True
            else:
                return False
                

        result = 0
        for word in words:
            if is_prefix(word, s):
                result += 1
            
        return result
        