class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int n = nums.size();
        if (n == 0)
            return 0;

        sort(nums.begin(), nums.end());

        int currSeq = 1;
        int maxSeq = 1;

        for (int i = 1; i < n; i++) {
            if (nums[i - 1] == nums[i])
                continue;

            else if (nums[i - 1] == (nums[i] - 1))
                currSeq++;

            else if (nums[i - 1] != (nums[i] - 1))
                currSeq = 1;

            maxSeq = max(maxSeq, currSeq);
        }

        return maxSeq;
    }
};