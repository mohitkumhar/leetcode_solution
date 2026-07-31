class Solution {
public:
    bool isPalindrome(int x) {

        string nums = to_string(x);

        int i = 0;
        int j = nums.size() - 1;

        while (i < j) {
            if (nums[i] != nums[j]) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
};