class Solution {
public:
    int maxProduct(int n) {
        string nums = to_string(n);
        vector<int> digits;

        for (char c : nums) {
            digits.push_back(c - '0');
        }

        sort(digits.rbegin(), digits.rend());

        return digits[0] * digits[1];
    }
};