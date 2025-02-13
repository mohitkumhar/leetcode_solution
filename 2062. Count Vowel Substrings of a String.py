class Solution:
    def countVowelSubstrings(self, word: str) -> int:

        k = 0

        vov = set('aeiou')

        count = 0

        i = 0

        def full_vowel(word, start, end):
            map = {
                'a': 0,
                'e': 0,
                'i': 0,
                'o': 0,
                'u': 0,
            }

            for char in range(start, end + 1):
                map[word[char]] += 1
            
            for val in map.values():
                if val < 1:
                    return False
            return True
            
        while k < len(word):
            
            if word[k] in vov:
                vov_arr = set(['a', 'e', 'i', 'o', 'u'])
                i = k

                while i < len(word) and word[i] in vov:
                    # print(word[k: i + 1])
                    if full_vowel(word, k, i):
                        count += 1
                        
                    
                    
                    i += 1




                if not vov_arr:
                    count += 1
                # print(count)
            


                
                
                i += 1

            
            k += 1
        
        return count
