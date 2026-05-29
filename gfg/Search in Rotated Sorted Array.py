from typing import List

class Solution:
    def search(self, arr, key):
        n = len(arr)
        left = 0
        right = n - 1
        
        def find_pivot(nums: List[int]) -> int:
            left = 0
            right = len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[right] > nums[mid]:
                    right = mid
                else:
                    left = mid + 1

            return left
    
        def binary_search(left: int, right: int, nums: List[int]) -> int:
            while left <= right:
                mid = left + (right - left) // 2
                
                if nums[mid] == key:
                    return mid
                
                elif nums[mid] < key:
                    left = mid + 1
                else:
                    right = mid - 1

            return -1

        pivot = find_pivot(arr)
        
        first_element = binary_search(0, pivot - 1, arr)
        second_element = binary_search(pivot, len(arr) - 1, arr)
        
        return max(first_element, second_element)
