class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int totalSum = accumulate(nums.begin(), nums.end(), 0);
        if (totalSum % 2 == 1)
            return false;

        int target = totalSum / 2;
        int n = nums.size();
        vector<vector<bool>> dp(n + 1, vector<bool>(target + 1, false));

        for (int i = 0; i <= n; i++) {
            dp[i][0] = true;
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= target; j++) {
                bool take = false;
                if (j >= nums[i - 1]) {
                    take = dp[i - 1][j - nums[i - 1]];
                }
                bool skip = dp[i - 1][j];

                dp[i][j] = take || skip;
            }
        }
        return dp[n][target];
    }
};