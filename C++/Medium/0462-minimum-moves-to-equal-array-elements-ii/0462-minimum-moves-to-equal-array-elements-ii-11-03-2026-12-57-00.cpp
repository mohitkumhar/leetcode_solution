class Solution {
public:
    int minMoves2(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        int n = nums.size();
        int median = -1;

        if (n % 2 == 1) {
            median = nums[n / 2];
        } else {
            median = (nums[n / 2] + nums[n / 2 - 1]) / 2;
        }

        int totalMoves = 0;

        for (int num: nums) {
            totalMoves += abs(median - num);
        }
        return totalMoves;



    }
};