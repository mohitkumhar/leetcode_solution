class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        vector<vector<int>> dp(n + 2, vector<int>(2, 0));

        for (int i = n - 1; i >= 0; i--) {
            int buyStock = dp[i + 1][1] - prices[i];
            int skipBuyStock = dp[i + 1][0];

            int sellStock = dp[i + 2][0] + prices[i];
            int skipSellStock = dp[i + 1][1];

            dp[i][0] = max({buyStock, skipBuyStock});
            dp[i][1] = max({sellStock, skipSellStock});
        }

        return dp[0][0];
    }
};