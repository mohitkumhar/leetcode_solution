class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int currSum = nums[0];
        int maxSum = nums[0];

        for (int i = 1; i < nums.size(); i++) {
            currSum = max(nums[i], nums[i] + currSum);
            maxSum = max(maxSum, currSum);
        }

        return maxSum;
    }
};