class Solution {
public:
    int helper(int goal, vector<int> nums) {
        if (goal < 0)
            return 0;

        int n = nums.size();

        int i = 0;
        int j = 0;

        int currSum = 0;
        int ans = 0;

        while (j < n) {
            currSum += nums[j];

            while (currSum > goal) {
                currSum -= nums[i];
                i++;
            }

            ans += (j - i + 1);
            j++;
        }
        return ans;
    }

    int numSubarraysWithSum(vector<int>& nums, int goal) {
        return helper(goal, nums) - helper(goal - 1, nums);
    }
};