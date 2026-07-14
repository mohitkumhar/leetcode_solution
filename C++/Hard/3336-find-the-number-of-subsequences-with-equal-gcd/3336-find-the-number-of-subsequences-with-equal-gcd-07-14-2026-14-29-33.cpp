class Solution {
public:
    int dp[201][201][201];
    const int MOD = 1e9 + 7;

    int subsequencePairCount(vector<int>& nums) {
        int dp[201][201][201];
        int maxVal = *max_element(nums.begin(), nums.end());
        int n = nums.size();

        for (int gcd_val_1 = 0; gcd_val_1 <= maxVal; gcd_val_1++) {
            for (int gcd_val_2 = 0; gcd_val_2 <= maxVal; gcd_val_2++) {
                if (gcd_val_1 == gcd_val_2 && gcd_val_1 != 0 && gcd_val_2) {
                    dp[n][gcd_val_1][gcd_val_2] = 1;
                } else {
                    dp[n][gcd_val_1][gcd_val_2] = 0;
                }
            }
        }

        for (int i = n - 1; i >= 0; i--) {
            for (int gcd_val_1 = 0; gcd_val_1 <= maxVal; gcd_val_1++) {
                for (int gcd_val_2 = 0; gcd_val_2 <= maxVal; gcd_val_2++) {

                    int skip = dp[i + 1][gcd_val_1][gcd_val_2];
                    int take_in_1 =
                        dp[i + 1][gcd(gcd_val_1, nums[i])][gcd_val_2];
                    int take_in_2 =
                        dp[i + 1][gcd_val_1][gcd(gcd_val_2, nums[i])];

                    dp[i][gcd_val_1][gcd_val_2] =
                        (0LL + skip + take_in_1 + take_in_2) % MOD;
                }
            }
        }

        return dp[0][0][0];
    }
};