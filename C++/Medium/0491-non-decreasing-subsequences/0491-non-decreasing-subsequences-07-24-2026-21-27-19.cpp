class Solution {
public:
    void backtrack(int i, int prev, vector<int> temp,
                   vector<vector<int>> &result, vector<int> nums) {
        unordered_set<int> seen;
        if (temp.size() >= 2)
            result.push_back(temp);
        if (i == nums.size())
            return;

        for (int k = i; k < nums.size(); k++) {
            if (seen.find(nums[k]) != seen.end())
                continue;
            if (prev != -1 && nums[k] < nums[prev])
                continue;
            seen.insert(nums[k]);
            temp.push_back(nums[k]);

            backtrack(k + 1, k, temp, result, nums);

            temp.pop_back();
        }
    }

    vector<vector<int>> findSubsequences(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> temp;

        backtrack(0, -1, temp, result, nums);

        return result;
    }
};