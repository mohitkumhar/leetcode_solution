class Solution {
public:
    vector<bool> pathExistenceQueries(int n, vector<int>& nums, int maxDiff,
                                      vector<vector<int>>& queries) {
        vector<int> component(n, -1);
        int compId = 0;
        component[0] = compId;
        for (int i = 1; i < n; i++) {
            if (nums[i] - nums[i - 1] > maxDiff) {
                compId++;
            }
            component[i] = compId;
        }

        vector<bool> result;
        for (auto& query : queries) {
            result.push_back(component[query[0]] == component[query[1]]);
        }
        return result;
    }
};
