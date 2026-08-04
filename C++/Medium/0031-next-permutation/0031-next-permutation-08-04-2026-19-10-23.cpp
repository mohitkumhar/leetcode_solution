class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size();

        int breakPoint = -1;

        for (int i = n - 1; i > 0; i--)
            if (nums[i - 1] < nums[i]) {
                breakPoint = i - 1;
                break;
            }

        if (breakPoint == -1) {
            reverse(nums.begin(), nums.end());
            return;
        }

        // find just greater element than breakpoint
        for (int j = n - 1; j > breakPoint; j--)
            if (nums[j] > nums[breakPoint]) {
                swap(nums[j], nums[breakPoint]);
                break;
            }

        // reverse the array from in this range
        int left = breakPoint + 1;
        int right = n - 1;

        while (left < right) {
            swap(nums[left], nums[right]);
            left++;
            right--;
        }
    }
};