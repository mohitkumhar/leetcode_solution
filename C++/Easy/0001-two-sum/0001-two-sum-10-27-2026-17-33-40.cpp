class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> counter;

        for (int i = 0; i < nums.size(); i++) {
            counter[nums[i]] = i;
        }

        for (int i = 0; i < nums.size(); i++) {
            int value = target - nums[i];

            if (counter.find(value) != counter.end() && i != counter[value]) {
                return {i, counter[value]};
            }
        }
        return {};
    }
};