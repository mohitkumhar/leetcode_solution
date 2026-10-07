class Solution {
public:
    int n;

    int solve(int i, vector<int>& days, vector<int>& costs, vector<int>& memo) {
        if (i >= n)
            return 0;

        if (memo[i] != -1)
            return memo[i];

        // day 1
        int cost_1 = costs[0] + solve(i + 1, days, costs, memo);

        // day 7
        int j = i;
        int maxDay = days[i] + 7;

        while (j < n && days[j] < maxDay)
            j++;

        int cost_7 = costs[1] + solve(j, days, costs, memo);

        // day 30
        j = i;
        maxDay = days[i] + 30;

        while (j < n && days[j] < maxDay)
            j++;

        int cost_30 = costs[2] + solve(j, days, costs, memo);

        return memo[i] = min({cost_1, cost_7, cost_30});
    }

    int mincostTickets(vector<int>& days, vector<int>& costs) {
        n = days.size();
        vector<int> memo(n + 1, -1);

        return solve(0, days, costs, memo);
    }
};