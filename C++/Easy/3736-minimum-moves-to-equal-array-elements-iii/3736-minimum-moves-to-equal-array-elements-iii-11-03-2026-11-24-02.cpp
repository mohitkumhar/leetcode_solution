class Solution {
public:
    int minMoves(vector<int>& nums) {
        int maxElement = *max_element(nums.begin(), nums.end());
        int totalMoves = 0;

        for (int num: nums) {
            totalMoves += maxElement - num;
        }
        return totalMoves;
    }
};