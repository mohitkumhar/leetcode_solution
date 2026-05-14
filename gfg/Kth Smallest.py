import heapq

class Solution:
    def kthSmallest(self, arr, k):
        
        def partition_array(low, high):
            pivot = arr[low]
            pivot_index = low
            
            while low <= high:
                if arr[low] > pivot and arr[high] < pivot:
                    arr[low], arr[high] = arr[high], arr[low]
                    low += 1
                    high -= 1
                
                if low <= high and arr[low] <= pivot:
                    low += 1
                
                if low <= high and arr[high] >= pivot:
                    high -= 1

            arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
            return high


        low = 0
        high = len(arr) - 1

        while True:
            pivot = partition_array(low, high)
            if pivot == k - 1:
                return arr[pivot]
            
            elif pivot > k - 1:
                high = pivot - 1
            
            elif pivot < k - 1:
                low = pivot + 1
        
        
        return -1
        
