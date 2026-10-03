class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        int total = 0;
        int current = 0;

        for (int i = 2; i < nums.size(); i++) {
            if (nums[i - 2] - nums[i - 1] == nums[i - 1] - nums[i]) {
                current++;
                total += current;
            } else
                current = 0;
        }
        return total;
    }
};