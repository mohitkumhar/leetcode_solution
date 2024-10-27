class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for string  in strs:
            sorted_string = ''.join(sorted(string))

            if sorted_string not in anagrams:
                anagrams[sorted_string] = []
            anagrams[sorted_string].append(string)
        
        return list(anagrams.values())
