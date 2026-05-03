class Solution:
    def sort012(self, arr):
        zeros = arr.count(0)
        ones = arr.count(1)
        twos = arr.count(2)
        
        i = 0
        for _ in range(zeros):
            arr[i] = 0
            i += 1
                    
        for _ in range(ones):
            arr[i] = 1
            i += 1
                    
        for _ in range(twos):
            arr[i] = 2
            i += 1
        
        return arr
