class Solution {
public:
    vector<int> memo;

    int solve(int i, int n, vector<int>& costs) {
        if (i >= n) return 0;
        if (memo[i] != -1) return memo[i];

        int ans = INT_MAX;
        for (int jump = 1; jump <= 3; ++jump) {
            int j = i + jump;
            if (j <= n) {
                ans = min(ans, costs[j - 1] + jump * jump + solve(j, n, costs));
            }
        }
        return memo[i] = ans;
    }

    int climbStairs(int n, vector<int>& costs) {
        memo.assign(n + 1, -1);
        return solve(0, n, costs);
    }
};