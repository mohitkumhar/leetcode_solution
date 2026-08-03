class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int target = (nums.size() / 2) + 1;

        sort(nums.begin(), nums.end());

        int count = 0;
        int prev = -1;

        for (int num : nums) {
            if (num != prev)
                count = 1;
            else
                count++;

            prev = num;

            if (count >= target)
                return num;
        }
        return 0;
    }
};