class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        for char in s:

            if char != ']':
                stack.append(char)

            else:
                curr_str = ''

                while stack and stack[-1] != '[':
                    curr_str = stack.pop() + curr_str
                    print(curr_str)
                    
                stack.pop()
                
                curr_num = ''
                while stack and stack[-1].isdigit():
                    curr_num = stack.pop() + curr_num
                
                curr_str = curr_str * int(curr_num)
                stack.append(curr_str)
            
        return ''.join(stack)