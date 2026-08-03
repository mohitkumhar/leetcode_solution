class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int n = nums.size();
        int count = 0;
        int maxOnes = 0;

        for (int num : nums) {
            if (num == 1) {
                count++;
                maxOnes = max(maxOnes, count);
            } else
                count = 0;
        }
        return maxOnes;
    }
};