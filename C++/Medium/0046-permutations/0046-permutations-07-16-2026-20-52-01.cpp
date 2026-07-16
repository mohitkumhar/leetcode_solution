class Solution {
public:
    vector<vector<int>> result;
    unordered_set<int> set;
    int n;

    void backtrack(vector<int>& temp, vector<int> nums) {
        if (temp.size() == n) {
            result.push_back(temp);
            return;
        }

        for (int i = 0; i < n; i++) {
            if (!set.contains(nums[i])) {
                set.insert(nums[i]);
                temp.push_back(nums[i]);

                backtrack(temp, nums);

                set.erase(nums[i]);
                temp.pop_back();
            }
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        n = nums.size();
        vector<int> temp;
        backtrack(temp, nums);

        return result;
    }
};