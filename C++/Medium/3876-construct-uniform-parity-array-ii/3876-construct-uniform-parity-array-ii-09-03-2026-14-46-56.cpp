class Solution {
public:
    bool uniformArray(vector<int>& nums1) {
        int minOdd = INT_MAX;
        int minEven = INT_MAX;

        for (int num : nums1) {
            if (num % 2 == 0)
                minEven = min(minEven, num);
            else
                minOdd = min(minOdd, num);
        }

        if (minEven == INT_MAX || minOdd == INT_MAX)
            return true;

        return minEven > minOdd;
    }
};