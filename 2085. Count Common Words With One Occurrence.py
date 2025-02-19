class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:

        words1_freq = {}
        words2_freq = {}

        for word in words1:
            if word in words1_freq:
                words1_freq[word] += 1
            
            else:
                words1_freq[word] = 1

        for word in words2:
            if word in words2_freq:
                words2_freq[word] += 1
            
            else:
                words2_freq[word] = 1

        ans = 0
        for word in words1:
            if words1_freq[word] == 1 and words2_freq.get(word, 0) == 1:
                ans += 1
        
        return ans
        