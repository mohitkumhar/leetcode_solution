class Solution {
public:
    int minimumSubarrayLength(vector<int>& nums, int k) {
        int n = nums.size();
        int ans = INT_MAX;

        for (int i = 0; i < n; i++) {
            int currOR = 0;

            for (int j = i; j < n; j++) {
                currOR |= nums[j];

                if (currOR >= k) {
                    ans = min(ans, j - i + 1);
                    break;
                }
            }
        }
        if (ans != INT_MAX)
            return ans;
        return -1;
    }
};