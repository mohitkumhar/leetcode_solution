class Solution {
public:
    int maxDistinct(string s) {
        unordered_set<char> nums(s.begin(), s.end());
        return nums.size();
    }
};