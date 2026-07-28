class Solution {
public:
    void backtrack(int i, map<int, int>& map, int& count, int k,
                   vector<int>& nums) {
        if (i >= nums.size()) {
            count++;
            return;
        }

        // skip
        backtrack(i + 1, map, count, k, nums);

        // take
        if (map.count(nums[i] + k) == 0 && map.count(nums[i] - k) == 0) {
            map[nums[i]]++;
            backtrack(i + 1, map, count, k, nums);
            map[nums[i]]--;
            if (map[nums[i]] == 0)
                map.erase(nums[i]);
        }
    }

    int beautifulSubsets(vector<int>& nums, int k) {
        int n = nums.size();

        map<int, int> map;
        int count = 0;

        backtrack(0, map, count, k, nums);

        return count -
               1; // use `-1` since it is counting the first empty subset
    }
};