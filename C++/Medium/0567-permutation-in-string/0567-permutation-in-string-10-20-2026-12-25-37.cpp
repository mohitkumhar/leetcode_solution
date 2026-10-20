class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int n = s1.size();
        int m = s2.size();

        if (n > m)
            return false;

        vector<int> s1Freq(26, 0);
        vector<int> s2Freq(26, 0);

        for (char ch : s1)
            s1Freq[ch - 'a']++;

        int i = 0;
        int j = 0;

        while (j < m) {
            s2Freq[s2[j] - 'a']++;

            if (j - i + 1 < n) {
                j++;
            } else if (j - i + 1 == n) {
                if (s1Freq == s2Freq)
                    return true;

                s2Freq[s2[i] - 'a']--;
                i++;
                j++;
            }
        }
        return false;
    }
};