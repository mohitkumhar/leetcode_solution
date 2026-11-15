class Solution {
public:
    int beautySum(string s) {

        int n = s.size();
        int count = 0;

        for (int i = 0; i < n; i++) {
            vector<int> freq(26, 0);

            int maxFreq = INT_MIN;

            for (int j = i; j < n; j++) {
                int idx = s[j] - 'a';
                freq[idx]++;

                maxFreq = max({maxFreq, freq[idx]});

                int minFreq = INT_MAX;
                for (int num : freq) {
                    if (num > 0)
                        minFreq = min({minFreq, num});
                }
                count += maxFreq - minFreq;
            }
        }
        return count;
    }
};