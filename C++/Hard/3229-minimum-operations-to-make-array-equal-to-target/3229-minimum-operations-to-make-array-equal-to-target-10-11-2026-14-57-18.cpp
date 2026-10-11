class Solution {
public:
    long long minimumOperations(vector<int>& nums, vector<int>& target) {
        long long result = 0;

        int prev = 0;
        int curr = 0;

        for (int i = 0; i < nums.size(); i++) {
            curr = target[i] - nums[i];

            if (prev > 0 && curr < 0 || prev < 0 && curr > 0) {
                result += abs(curr);
            } else if (abs(curr) > abs(prev))
                result += abs(prev - curr);
            prev = curr;
        }
        return result;
    }
};