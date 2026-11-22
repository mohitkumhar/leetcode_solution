class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        int maxReachable = 0;

        for (int i = 0; i < nums.size(); i++) {
            if (i > maxReachable)
                return false;
            if (i == n - 1)
                return true;

            maxReachable = max(maxReachable, i + nums[i]);
        }
        return false;
    }
};