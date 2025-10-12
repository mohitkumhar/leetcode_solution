class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        map = {}
        for piece in pieces:
            map[piece[0]] = piece
        i = 0
        while i < len(arr):
            if arr[i] not in map:
                return False
            
            for val in map[arr[i]]:
                if val != arr[i]:
                    return False    
                i += 1
        return True