class Solution {
public:
    int takeCharacters(string s, int k) {
        int n = s.size();

        int a_count = 0;
        int b_count = 0;
        int c_count = 0;

        for (char ch: s) {
            if (ch == 'a') a_count++;
            if (ch == 'b') b_count++;
            if (ch == 'c') c_count++;
        }

        if (a_count < k || b_count < k || c_count < k)
            return -1;

        int i = 0;
        int j = 0;
        int result = 0;

        while (j < n) {
            if (s[j] == 'a') a_count--;
            if (s[j] == 'b') b_count--;
            if (s[j] == 'c') c_count--;

            while (i <= j && (a_count < k || b_count < k || c_count < k)) {
                if (s[i] == 'a') a_count++;
                if (s[i] == 'b') b_count++;
                if (s[i] == 'c') c_count++;
                i++;
            }
            result = max(result, j - i + 1);
            j++;
        }
        return n - result;

    }
};