class Solution {
public:
    int solve(vector<int> nums, int k) {
        unordered_map<int, int> seen;
        int n = nums.size();

        int i = 0;
        int j = 0;

        int count = 0;

        while (j < n) {
            seen[nums[j]]++;

            while (seen.size() > k) {
                seen[nums[i]]--;
                if (seen[nums[i]] == 0)
                    seen.erase(nums[i]);
                i++;
            }
            count += j - i + 1;
            j++;
        }

        return count;
    }

    int subarraysWithKDistinct(vector<int>& nums, int k) {
        return solve(nums, k) - solve(nums, k - 1);
    }
};