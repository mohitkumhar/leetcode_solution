class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

        count_stack = [num for num in range(1, n + 1)]

        stack = []
        i = 0
        check_len = len(target)
        
        for num in count_stack:
            if num in target:
                i += 1
                stack.append("Push")
            else:
                stack.append("Push")
                stack.append("Pop")
            
            if i == check_len:
                break
        
        return stack
    
