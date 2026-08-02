class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        unordered_set<int> seen;

        int k = 0;

        for (int i = 0; i < n; i++) {
            if (seen.find(nums[i]) == seen.end()) {
                nums[k] = nums[i];
                k++;
                seen.insert(nums[i]);
            }
        }

        return k;
    }
};