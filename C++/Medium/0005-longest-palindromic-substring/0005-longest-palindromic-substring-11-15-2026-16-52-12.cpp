class Solution {
public:
    string expand(int left, int right, string s) {
        while (0 <= left && right < s.size()) {
            if (s[left] != s[right])
                break;
            left--;
            right++;
        }
        return s.substr(left + 1, right - left - 1);
    }

    string longestPalindrome(string s) {
        int n = s.size();

        string ans = "";

        for (int i = 0; i < n; i++) {
            string odd = expand(i, i, s);
            string even = expand(i, i + 1, s);

            if (odd.size() > ans.size())
                ans = odd;
            if (even.size() > ans.size())
                ans = even;
        }
        return ans;
    }
};