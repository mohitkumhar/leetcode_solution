class Solution {
public:
    int n = 0;
    // vector<vector<int>> memo;
    int memo[21][10002];

    int solve(int i, int diff, vector<int>& rods) {
        if (i >= n) {
            if (diff == 0)
                return 0;
            return INT_MIN;
        }

        if (memo[i][5000 + diff] != -1) return memo[i][5000 + diff];

        // take l1
        int take_l1 = rods[i] + solve(i + 1, diff + rods[i], rods);

        // take l2
        int take_l2 = rods[i] + solve(i + 1, diff - rods[i], rods);

        // take nothing
        int take_nothing = solve(i + 1, diff, rods);

        memo[i][5000 + diff] = max({take_l1, take_l2, take_nothing});

        return memo[i][5000 + diff];
    }

    int tallestBillboard(vector<int>& rods) {
        n = rods.size();

        memset(memo, -1, sizeof(memo));

        return solve(0, 0, rods) / 2;
    }
};