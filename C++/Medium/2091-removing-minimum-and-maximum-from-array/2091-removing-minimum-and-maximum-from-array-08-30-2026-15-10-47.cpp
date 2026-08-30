class Solution {
public:
    int minimumDeletions(vector<int>& nums) {

        int n = nums.size();

        int minIndex = min_element(nums.begin(), nums.end()) - nums.begin();
        int maxIndex = max_element(nums.begin(), nums.end()) - nums.begin();

        // delete both from left
        int left = 1 + max(minIndex, maxIndex);

        // delete both from right
        int right = n - min(minIndex, maxIndex);

        // delete from both end
        int mixed = 1 + min(minIndex, maxIndex) + n - max(minIndex, maxIndex);

        return min({left, right, mixed});
    }
};