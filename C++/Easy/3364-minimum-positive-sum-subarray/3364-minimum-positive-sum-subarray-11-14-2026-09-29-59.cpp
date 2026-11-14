class Solution {
public:
    int minimumSumSubarray(vector<int>& nums, int l, int r) {
        int n = nums.size();
        int minSum = INT_MAX;

        for (int i = 0; i < n; i++) {
            int currSum = 0;
            for (int j = i; j < n; j++) {
                currSum += nums[j];
                if (l <= j - i + 1 && r >= j - i + 1) {
                    if (currSum > 0)
                        minSum = min({minSum, currSum});
                }
            }
        }
        if (minSum == INT_MAX)
            return -1;
        return minSum;
    }
};