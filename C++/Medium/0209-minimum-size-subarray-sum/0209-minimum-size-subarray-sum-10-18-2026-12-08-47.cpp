class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int i = 0;
        int j = 0;
        int ans = INT_MAX;

        int n = nums.size();
        int currSum = 0;

        while (j < n) {
            currSum += nums[j];

            while (currSum >= target) {
                ans = min(ans, j - i + 1);
                currSum -= nums[i++];
            }
            j++;
        }
        return ans == INT_MAX ? 0 : ans;
    }
};