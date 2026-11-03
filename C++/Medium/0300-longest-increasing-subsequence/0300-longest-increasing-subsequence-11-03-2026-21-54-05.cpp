class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();

        vector<int> LIS(n, 1);
        int max_lis = 1;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    LIS[i] = max(LIS[i], LIS[j] + 1);
                    max_lis = max(max_lis, LIS[i]);
                }
            }
        }
        return max_lis;
    }
};