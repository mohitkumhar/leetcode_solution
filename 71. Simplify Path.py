class Solution:
    def simplifyPath(self, path: str) -> str:

        path_list = path.split('/')

        stack = []

        for path in path_list:
            if path:
                if path == '.':
                    continue
                
                elif path == '..':
                    if stack:
                        stack.pop()
                
                elif path == '...':
                    stack.append('...')
                
                else:
                    stack.append(path)
            

            
        return '/' + '/'.join(stack)
