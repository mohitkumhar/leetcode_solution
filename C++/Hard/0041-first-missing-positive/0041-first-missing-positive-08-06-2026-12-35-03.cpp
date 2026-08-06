class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();

        bool is1Present = find(nums.begin(), nums.end(), 1) != nums.end();

        if (is1Present == false)
            return 1;

        for (int i = 0; i < n; i++)
            if (nums[i] <= 0)
                nums[i] = 1;

        for (int i = 0; i < n; i++) {
            int num = abs(nums[i]);

            if ((num - 1) < n)
                nums[num - 1] = -abs(nums[num - 1]);
        }

        for (int i = 0; i < n; i++) {
            if (nums[i] < 0)
                continue;

            return i + 1;
        }

        return n + 1;
    }
};