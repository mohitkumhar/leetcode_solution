class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def first():
            left = 0
            right = len(nums) - 1
            ans = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    ans = mid
                    right = mid - 1
                
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return ans
        
        def second():
            left = 0
            right = len(nums) - 1
            ans = -1

            while left <= right:
                mid = left + (right - left) // 2
                
                if nums[mid] == target:
                    ans = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return ans
        
        return [first(), second()]


