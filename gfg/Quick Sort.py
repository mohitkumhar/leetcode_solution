class Solution:
    def quickSort(self, arr, low, high):
        
        def solve(low, high):
            if low >= high:
                return
            
            pivot = self.partition(arr, low, high)
            
            left_sorted = solve(low, pivot - 1)
            right_sorted = solve(pivot + 1, high)
        
        solve(low, high)
        

    def partition(self, arr, low, high):
        pivot = arr[high]
        k = low

        for i in range(low, high + 1):
            if arr[i] < pivot:
                arr[i], arr[k] = arr[k], arr[i]
                k += 1
    
        arr[k], arr[high] = arr[high], arr[k]
        
        return k
