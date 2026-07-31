class Solution {
public:
    bool isPalindrome(int x) {
        int original = x;
        long reversed = 0;

        while (x > 0) {
            int digit = x % 10;
            reversed = (10 * reversed) + digit;
            x = x / 10;
        }

        if (original == reversed)
            return true;
        return false;
    }
};