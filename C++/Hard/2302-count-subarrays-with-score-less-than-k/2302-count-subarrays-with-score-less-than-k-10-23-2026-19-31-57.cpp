class Solution {
public:
    long long countSubarrays(vector<int>& nums, long long k) {
        int n = nums.size();

        int i = 0;
        int j = 0;

        long long currSum = 0;
        long long currProd = 0;
        long long count = 0;

        while (j < n) {
            currSum += nums[j];

            currProd = currSum * (j - i + 1);

            while (currProd >= k) {
                currSum -= nums[i];
                i++;
                currProd = currSum * (j - i + 1);
            }

            count += j - i + 1;

            j++;
        }
        return count;
    }
};