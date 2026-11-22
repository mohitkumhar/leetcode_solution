class Solution {
public:
    int countDominantElements(vector<int>& nums) {
        int n = nums.size();
        int count = 0;

        for (int i = 0; i < n; i++) {
            if (i == 0 && i == n - 1) {
                count++;
            } else if (i == 0) {
                if (nums[i] >= nums[i + 1])
                    count++;
            } else if (i == n - 1) {
                if (nums[i] >= nums[i - 1])
                    count++;
            } else {
                float avg = (nums[i - 1] + nums[i + 1]) / 2.0;
                if (nums[i] >= avg)
                    count++;
            }
        }
        return count;
    }
};