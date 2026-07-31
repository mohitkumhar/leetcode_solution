class Solution {
public:
    int reverse(int x) {
        int sign = 1;

        string s = to_string(x);

        if (s[0] == '-') {
            sign = -1;
            s = s.substr(1);
        }

        std::reverse(s.begin(), s.end());

        long long ans = stoll(s);
        ans *= sign;

        if (ans > INT_MAX || ans < INT_MIN)
            return 0;
        else
            return ans;
    }
};