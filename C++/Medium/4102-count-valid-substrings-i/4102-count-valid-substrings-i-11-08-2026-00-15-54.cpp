class Solution {
public:
    long long countValidSubstrings(string s) {
        int n = s.size();

        int i = 0;
        int j = 0;

        long long result = 0;

        while (j < n) {

            if (j >= 2 && s[j - 2] == 'a' && s[j - 1] == 'b' && s[j] == 'c')
                i = j - 1;

            result += (j - i + 1);
            j++;
        }

        return result;
    }
};