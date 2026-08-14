class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int n = nums.size();

        int left = 0;
        int right = n - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == nums[mid + 1]) {
                if ((right - mid) % 2 == 1)
                    right = mid - 1;
                else
                    left = mid + 2;
            } else {
                if ((right - mid) % 2 == 1)
                    left = mid + 1;
                else
                    right = mid;
            }
        }
        return nums[right];
    }
};