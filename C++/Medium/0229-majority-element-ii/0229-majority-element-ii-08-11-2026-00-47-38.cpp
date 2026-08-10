class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {

        int n = nums.size();
        int target = n / 3;

        vector<int> result;
        map<int, int> freq;

        for (int num : nums)
            freq[num]++;

        for (auto val : freq)
            if (val.second > target)
                result.push_back(val.first);
        return result;
    }
};