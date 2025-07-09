class Solution:
    def interpret(self, command: str) -> str:
        answer = ''

        for i in range(len(command)):
            if command[i] == 'G':
                answer += "G"
            elif command[i] == '(' and command[i + 1] == ')':
                answer += 'o'
            elif command[i] == '(' and command[i + 1] == 'a':
                answer += 'al'

        return answer