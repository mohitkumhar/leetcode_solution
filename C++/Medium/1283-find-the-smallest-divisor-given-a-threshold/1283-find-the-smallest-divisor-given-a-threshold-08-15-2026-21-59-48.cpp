class Solution {
public:
    bool isPossible(int val, vector<int> nums, int threshold) {
        int count = 0;

        for (int num : nums) {
            int flag = 0;
            if (num % val != 0)
                flag = 1;

            count += (num / val) + flag;
        }

        return count <= threshold;
    }

    int smallestDivisor(vector<int>& nums, int threshold) {
        int left = 1;
        int right = *max_element(nums.begin(), nums.end());

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (isPossible(mid, nums, threshold))
                right = mid;
            else
                left = mid + 1;
        }

        return left;
    }
};