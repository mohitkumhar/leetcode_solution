class Solution {
public:
    int targetSum = 0;
    vector<vector<int>> memo;

    bool solve(int i, int currSum, vector<int>& nums) {
        if (currSum == targetSum)
            return true;

        if (i >= nums.size() || currSum > targetSum)
            return false;

        if (memo[i][currSum] != -1)
            return memo[i][currSum];

        bool take = solve(i + 1, currSum + nums[i], nums);
        bool skip = solve(i + 1, currSum, nums);

        return memo[i][currSum] = take || skip;
    }

    bool canPartition(vector<int>& nums) {
        int sum = accumulate(nums.begin(), nums.end(), 0);

        if (sum % 2 != 0)
            return false;

        targetSum = sum / 2;

        memo.assign(nums.size(), vector<int>(targetSum + 1, -1));

        return solve(0, 0, nums);
    }
};