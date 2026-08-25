class Solution {
public:
    int missingMultiple(vector<int>& nums, int k) {
        
        unordered_set<int> numsSet = unordered_set(nums.begin(), nums.end());

        for (int i = 1; i <= *max_element(nums.begin(), nums.end()) + k; i++) {
            if (!numsSet.contains(i) && i % k == 0) {
                return i;
            }
        }

        return -1;

    }
};