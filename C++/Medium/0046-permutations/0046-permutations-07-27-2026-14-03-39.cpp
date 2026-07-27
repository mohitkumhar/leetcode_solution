class Solution {
public:
    unordered_set<int> seen;
    int n;

    void backtrack(int i, vector<int>& curr_perm, vector<int>& nums,
                   vector<vector<int>>& result) {
        if (curr_perm.size() == nums.size()) {
            result.push_back(curr_perm);
            return;
        }

        for (int j = 0; j < n; j++) {
            if (seen.find(nums[j]) != seen.end())
                continue;

            seen.insert(nums[j]);
            curr_perm.push_back(nums[j]);

            backtrack(j + 1, curr_perm, nums, result);

            seen.erase(nums[j]);
            curr_perm.pop_back();
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        vector<int> curr_perm;
        vector<vector<int>> result;

        n = nums.size();

        backtrack(0, curr_perm, nums, result);
        return result;
    }
};