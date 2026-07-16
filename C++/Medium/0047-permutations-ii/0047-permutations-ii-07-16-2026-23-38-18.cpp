class Solution {
public:
    vector<vector<int>> result;
    int n;
    map<int, int> mp;

    void backtrack(vector<int> temp) {
        if (temp.size() == n) {
            result.push_back(temp);
            return;
        }

        for (auto& num : mp) {
            if (num.second > 0) {
                num.second--;
                temp.push_back(num.first);

                backtrack(temp);

                temp.pop_back();
                num.second++;
            }
        }
    }

    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<int> temp;
        n = nums.size();

        for (int num : nums) {
            mp[num]++;
        }

        backtrack(temp);

        return result;
    }
};