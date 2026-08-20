class Solution {
public:
    bool isPossible(int maxVal, vector<int> nums, int k) {
        int currVal = 0;
        int subArrayCount = 1;

        for (int num : nums) {
            if ((currVal + num) > maxVal) {
                subArrayCount++;
                currVal = num;
            } else
                currVal += num;
        }
        return subArrayCount <= k;
    }

    int splitArray(vector<int>& nums, int k) {
        int left = *max_element(nums.begin(), nums.end());
        int right = accumulate(nums.begin(), nums.end(), 0);

        int ans = 0;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (isPossible(mid, nums, k)) {
                ans = mid;
                right = mid - 1;
            } else
                left = mid + 1;
        }
        return ans;
    }
};