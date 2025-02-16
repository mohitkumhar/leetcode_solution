    class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        
        map = {}

        i = 0
        for width in widths:
            map[chr(97 + i)] = width
            i += 1
        
        line = 1
        temp_width = 0

        for char in s:
            char_width = map[char]

            if temp_width + char_width > 100:
                line += 1
                temp_width = char_width
            
            else:
                temp_width += char_width
        
        return [line, temp_width]
