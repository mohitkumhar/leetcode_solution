class Solution {
public:
    int minFlips(string s) {
        int n = s.size();
        s += s;

        string s1 = "";
        string s2 = "";

        for (int i = 0; i < 2 * n; i++) {
            s1 += (i % 2 == 0 ? "1" : "0");
            s2 += (i % 2 == 1 ? "1" : "0");
        }

        int count1 = 0;
        int count2 = 0;
        int result = INT_MAX;

        int i = 0;
        int j = 0;

        while (j < 2 * n) {
            if (s[j] != s1[j])
                count1++;
            if (s[j] != s2[j])
                count2++;

            if (j - i + 1 > n) {
                if (s[i] != s1[i])
                    count1--;
                if (s[i] != s2[i])
                    count2--;
                i++;
            }

            if (j - i + 1 == n)
                result = min({result, count1, count2});

            j++;
        }

        return result;
    }
};