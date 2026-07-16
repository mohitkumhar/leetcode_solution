class Solution {
public:
    long long gcdSum(vector<int>& nums) {
        int n = nums.size();
        int maxSeen = 0;

        for (int i = 0; i < n; i++) {
            if (nums[i] > maxSeen) {
                maxSeen = nums[i];
            }
            nums[i] = __gcd(nums[i], maxSeen);
        }

        int i = 0;
        int j = n - 1;
        long long result = 0;
        sort(nums.begin(), nums.end());

        while (i < j) {
            result += __gcd(nums[i], nums[j]);
            i++;
            j--;
        }

        return result;
    }
};