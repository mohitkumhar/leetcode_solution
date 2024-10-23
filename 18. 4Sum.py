class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        result = []

        n = len(nums)

        for i in range(n - 3):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                low, high = j + 1, n - 1

                while low < high:
                    current_sum = nums[i] + nums[j] + nums[low] + nums[high]

                    if current_sum == target:
                        result.append([nums[i], nums[j], nums[low], nums[high]])

                        while low < high and nums[low] == nums[low + 1]:
                            low += 1
                        while low < high and nums[high] == nums[high - 1]:
                            high -= 1
                        
                        low += 1
                        high -= 1
                    
                    elif current_sum < target:
                        low += 1
                    else:
                        high -= 1
                
        return result
