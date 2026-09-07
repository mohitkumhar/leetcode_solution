#include <numeric>

class Solution {
public:
    int distinctSubseqII(string s) {
        long long MOD = 1e9 + 7;
        vector<long long> dp(26, 0);

        for (char ch : s) {
            int idx = ch - 'a';
            dp[idx] = (accumulate(dp.begin(), dp.end(), 0LL) + 1) % MOD;
        }
        return (accumulate(dp.begin(), dp.end(), 0LL)) % MOD;
    }
};