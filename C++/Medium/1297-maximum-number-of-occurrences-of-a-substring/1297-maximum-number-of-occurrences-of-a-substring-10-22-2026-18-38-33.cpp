class Solution {
public:
    int maxFreq(string s, int maxLetters, int minSize, int maxSize) {
        int n = s.size();

        int i = 0;
        int j = 0;

        int ans = 0;

        unordered_map<char, int> charFreq;
        unordered_map<string, int> freq;

        while (j < n) {
            charFreq[s[j]]++;

            if (j - i + 1 > minSize) {
                charFreq[s[i]]--;
                if (charFreq[s[i]] == 0)
                    charFreq.erase(s[i]);
                i++;
            }

            if (j - i + 1 <= maxSize && j - i + 1 >= minSize) {
                if (charFreq.size() <= maxLetters) {
                    string substring = s.substr(i, j - i + 1);
                    freq[substring]++;
                    ans = max(ans, freq[substring]);
                }
            }
            j++;
        }
        return ans;
    }
};