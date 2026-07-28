class Solution {
public:
    string smallestPalindrome(string s) {
        int n = s.size();

        int mid = n / 2;

        sort(s.begin(), s.begin() + mid);

        int i = 0;
        int j = n - 1;

        while (i < j) {
            s[j] = s[i];
            i++;
            j--;
        }

        return s;
    }
};