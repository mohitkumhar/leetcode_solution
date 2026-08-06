class Solution {
public:
    bool isValid(vector<int> nums, int maxVal, int k) {
        int count = 1;
        long currSum = 0;

        for (int num : nums) {
            if ((currSum + num) > maxVal) {
                count++;
                currSum = num;
            } else
                currSum += num;
        }

        return count <= k;
    }

    int splitArray(vector<int>& nums, int k) {

        int left = *max_element(nums.begin(), nums.end());
        int right = accumulate(nums.begin(), nums.end(), 0);

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (isValid (nums, mid, k))
                right = mid;
            else
                left = mid + 1;
        }
        return right;
    }
};