class Solution {
public:
    int maximumStrongPairXor(vector<int>& nums) {
        int ans = 0;
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int x = nums[i];
                int y = nums[j];

                if (abs(x - y) <= min(x, y))
                    ans = max(ans, x ^ y);
            }
        }
        return ans;
    }
};