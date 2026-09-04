class Solution {
public:
    int myAtoi(string s) {

        int i = 0;
        long long result = 0;
        int n = s.size();
        int sign = 1;

        while (i < n && s[i] == ' ')
            i++;

        if (i < n && (s[i] == '-' || s[i] == '+')) {
            if (s[i] == '-')
                sign = -1;
            i++;
        }

        while (i < n && isdigit(s[i])) {
            result = result * 10 + (s[i] - '0');

            if (sign == 1 && result > INT_MAX)
                return INT_MAX;

            if (sign == -1 && -result < INT_MIN)
                return INT_MIN;

            i++;
        }

        result *= sign;

        if (result < INT_MIN)
            return INT_MIN;
        if (result > INT_MAX)
            return INT_MAX;
        return result;
    }
};