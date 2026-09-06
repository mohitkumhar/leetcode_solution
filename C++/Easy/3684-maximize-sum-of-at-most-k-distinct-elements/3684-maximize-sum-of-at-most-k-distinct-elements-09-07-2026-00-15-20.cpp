class Solution {
public:
    vector<int> maxKDistinct(vector<int>& nums, int k) {
        set<int, greater<int>> s(nums.begin(), nums.end());

        vector<int> ans;

        for (int x : s) {
            if (ans.size() == k)
                break;
            ans.push_back(x);
        }

        return ans;
    }
};