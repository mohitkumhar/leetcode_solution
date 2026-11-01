class Solution {
public:
    int minMoves(vector<int>& nums) {
        int minElement = *min_element(nums.begin(), nums.end());
        int totalOp = 0;

        for (int num : nums) {
            totalOp += num - minElement;
        }
        return totalOp;
    }
};