class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n = nums.size();
        int result = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j)
                    continue;
                result = max(result, (nums[i] - 1) * (nums[j] - 1));
            }
        }
        return result;
    }
};