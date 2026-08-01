class Solution {
public:
    void binary_search(int target_idx, int& ans, int k, const vector<int> &nums,
                      const vector<long long> &prefix_sum) {
        int left = 0;
        int right = target_idx;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            long long final_sum = 1LL * nums[target_idx] * (target_idx - mid + 1);
            long long curr_sum = 0;

            if (mid == 0)
                curr_sum = prefix_sum[target_idx];
            else
                curr_sum = prefix_sum[target_idx] - prefix_sum[mid - 1];

            long long total_operation = final_sum - curr_sum;

            if (total_operation <= k) {
                ans = max(ans, target_idx - mid + 1);
                right = mid - 1;
            } else
                left = mid + 1;
        }
    }

    int maxFrequency(vector<int>& nums, int k) {

        sort(nums.begin(), nums.end());

        vector<long long> prefix_sum(nums.size(), 0);

        prefix_sum[0] = nums[0];

        for (int i = 1; i < prefix_sum.size(); i++)
            prefix_sum[i] = prefix_sum[i - 1] + nums[i];

        int ans = 0;

        for (int i = 0; i < nums.size(); i++)
            binary_search(i, ans, k, nums, prefix_sum);

        return ans;
    }
};