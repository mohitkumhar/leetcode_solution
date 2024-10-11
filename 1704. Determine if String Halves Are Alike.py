class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        vovel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        s_list = list(s)

        split_length = len(s_list) // 2

        s_1 = s_list[:split_length]
        s_2 = s_list[split_length:]

        s_1_count = 0
        s_2_count = 0
    
        for i in s_1:
            if i in vovel:
                s_1_count += 1
        
        for i in s_2:
            if i in vovel:
                s_2_count += 1
        
        return s_1_count == s_2_count
