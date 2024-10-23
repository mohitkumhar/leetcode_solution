class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        nums.sort()

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            low, high = i + 1, n - 1

            while low < high:
                current_sum = nums[i] + nums[low] + nums[high]

                if current_sum == 0:
                    result.append([nums[i], nums[low], nums[high]])

                    while low < high and nums[low] == nums[low + 1]:
                        low += 1

                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1
                    
                    low += 1
                    high -= 1
                    
                elif current_sum < 0:
                    low += 1
                else:
                    high -= 1
                
        
        return result