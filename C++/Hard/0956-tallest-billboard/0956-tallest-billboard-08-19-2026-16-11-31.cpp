class Solution {
public:
    int n = 0;

    int solve(int i, int diff, vector<int> &rods) {
        if (i >= n) {
            if (diff == 0)
                return 0;
            return INT_MIN;
        }

        // take l1
        int take_l1 = rods[i] + solve(i + 1, diff + rods[i], rods);

        // take l2
        int take_l2 = rods[i] + solve(i + 1, diff - rods[i], rods);

        // take nothing
        int take_nothing = solve(i + 1, diff, rods);

        return max({take_l1, take_l2, take_nothing});
    }

    int tallestBillboard(vector<int>& rods) {
        n = rods.size();

        return solve(0, 0, rods) / 2;
    }
};