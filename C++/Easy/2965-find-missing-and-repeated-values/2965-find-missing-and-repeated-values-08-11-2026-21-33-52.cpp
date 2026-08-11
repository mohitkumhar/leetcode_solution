class Solution {
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {
        int n = grid.size();

        // Find duplicate
        int duplicate = -1;
        unordered_set<int> seen;

        for (auto& lst : grid) {
            for (int num : lst) {
                if (seen.count(num))
                    duplicate = num;
                else
                    seen.insert(num);
            }
        }

        // Find missing number
        int missingNumber = -1;

        for (int i = 1; i <= n * n; i++) {
            if (!seen.count(i)) {
                missingNumber = i;
                break;
            }
        }
        return {duplicate, missingNumber};
    }
};