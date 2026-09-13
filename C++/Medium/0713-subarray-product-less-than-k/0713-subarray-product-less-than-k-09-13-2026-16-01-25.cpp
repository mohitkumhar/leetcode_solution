class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        if (k <= 1)
            return 0;

        long long prod = 1;
        int n = nums.size();

        int i = 0;
        int j = 0;

        int count = 0;

        while (j < n) {
            prod *= nums[j];

            while (prod >= k) {
                prod /= nums[i];
                i++;
            }
            count += (j - i + 1);
            j++;
        }

        return count;
    }
};