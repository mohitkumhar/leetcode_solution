class Solution {
public:
    int longestAlternatingSubarray(vector<int>& nums, int threshold) {
        int n = nums.size();
        int ans = 0;

        for (int i = 0; i < n; i++) {
            if (nums[i] > threshold || nums[i] % 2 != 0)
                continue;

            for (int j = i; j < n; j++) {
                if (nums[j] > threshold)
                    break;

                if (j > i && nums[j] % 2 == nums[j - 1] % 2)
                    break;

                ans = max(ans, j - i + 1);
            }
        }
        return ans;
    }
};