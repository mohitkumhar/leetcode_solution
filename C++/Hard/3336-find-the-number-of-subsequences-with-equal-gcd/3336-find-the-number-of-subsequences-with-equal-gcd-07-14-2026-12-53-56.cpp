class Solution {
public:
    int memo[201][201][201];
    const int MOD = 1e9 + 7;

    int solve(vector<int>& nums, int i, int gcd_1, int gcd_2) {
        if (i == nums.size()) {
            if (gcd_1 == gcd_2 && gcd_1 != 0 && gcd_2 != 0) {
                return 1;
            } else {
                return 0;
            }
        } else if (memo[i][gcd_1][gcd_2] != -1) {
            return memo[i][gcd_1][gcd_2];
        }

        int skip = solve(nums, i + 1, gcd_1, gcd_2);
        int take_in_1 = solve(nums, i + 1, gcd(gcd_1, nums[i]), gcd_2);
        int take_in_2 = solve(nums, i + 1, gcd_1, gcd(nums[i], gcd_2));

        return memo[i][gcd_1][gcd_2] =
                   (0LL + skip + take_in_1 + take_in_2) % MOD;
    }

    int subsequencePairCount(vector<int>& nums) {
        memset(memo, -1, sizeof(memo));

        return solve(nums, 0, 0, 0) % MOD;
    }
};