class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();

        int buyCost = INT_MAX;
        int maxProfit = 0;

        for (int price : prices) {
            buyCost = min(buyCost, price);
            int profit = price - buyCost;
            maxProfit = max(maxProfit, profit);
        }

        return maxProfit;
    }
};