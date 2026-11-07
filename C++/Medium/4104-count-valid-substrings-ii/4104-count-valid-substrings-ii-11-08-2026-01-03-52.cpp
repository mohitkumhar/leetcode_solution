class Solution {
public:
    long long countValidSubstrings(string s) {
        int n = s.size();

        int last_a = -1;
        int last_ab = -1;

        int i = 0;
        int j = 0;

        long long result = 0;

        while (j < n) {
            if (s[j] == 'a') {
                last_a = j;
            } else if (s[j] == 'b') {
                if (last_a != -1)
                    last_ab = last_a;
            } else if (s[j] == 'c') {
                if (last_ab != -1)
                    i = max(i, last_ab + 1);
            }

            result += j - i + 1;
            j++;
        }
        return result;
    }
};