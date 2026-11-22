class Solution {
public:
    int n;
    vector<vector<int>> memo;

    int solve(int i, bool bought, vector<int>& prices) {
        if (i >= n) {
            return 0;
        }
        if (memo[i][bought] != -1)
            return memo[i][bought];

        int buyStock = 0;
        if (!bought)
            buyStock = solve(i + 1, true, prices) - prices[i];
        int skipBuyStock = solve(i + 1, bought, prices);

        int sellStock = 0;
        if (bought)
            sellStock = solve(i + 2, false, prices) + prices[i];
        int skipSellStock = solve(i + 1, bought, prices);

        return memo[i][bought] = max({buyStock, skipBuyStock, sellStock, skipSellStock});
    }

    int maxProfit(vector<int>& prices) {
        n = prices.size();

        memo.assign(n + 2, vector<int>(2, -1));

        return solve(0, false, prices);
    }
};