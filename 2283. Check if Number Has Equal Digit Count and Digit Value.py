class Solution:
    def digitCount(self, num: str) -> bool:
        
        map = {}
        
        for n in num:
            if n in map:
                map[n] += 1
            else:
                map[n] = 1

        for i in range(len(num)):
            if str(i) in map:
                if int(num[i]) != map[str(i)]:
                    return False
                
            else:
                if int(num[i]) != 0:
                    return False                                            

                
        
        return True
        