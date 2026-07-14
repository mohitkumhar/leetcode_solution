class Solution {
public:
    int memo[201][10001];

    bool solve(int i, int currSum, int target, vector<int>& nums) {
        if (currSum == target) {
            return true;
        } else if (i >= nums.size()) {
            return false;
        } else if (memo[i][currSum] != -1) {
            if (memo[i][currSum] == 1)
                return true;
            return false;
        }

        bool take = false;
        if ((nums[i] + currSum) <= target) {
            take = solve(i + 1, currSum + nums[i], target, nums);
        }
        bool skip = solve(i + 1, currSum, target, nums);

        bool ans = take || skip;
        if (ans == true) {
            memo[i][currSum] = true;
        } else {
            memo[i][currSum] = false;
        }
        return ans;
    }

    bool canPartition(vector<int>& nums) {
        int totalSum = accumulate(nums.begin(), nums.end(), 0);
        if (totalSum % 2 == 1)
            return false;

        int target = totalSum / 2;
        cout << totalSum << endl << target << endl;
        memset(memo, -1, sizeof(memo));

        return solve(0, 0, target, nums);
    }
};