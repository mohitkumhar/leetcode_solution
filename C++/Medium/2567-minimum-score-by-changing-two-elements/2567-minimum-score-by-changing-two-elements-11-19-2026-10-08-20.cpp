class Solution {
public:
    int minimizeSum(vector<int>& nums) {
        int n = nums.size();
        sort(nums.begin(), nums.end());

        int ans = min(
            {
                nums[n - 1] - nums[2],
                nums[n - 2] - nums[1],
                nums[n - 3] - nums[0]
            }
        );

        return ans;
    }
};