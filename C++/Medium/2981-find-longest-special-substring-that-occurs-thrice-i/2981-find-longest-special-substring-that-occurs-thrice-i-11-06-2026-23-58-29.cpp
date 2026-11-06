class Solution {
public:
    int maximumLength(string s) {
        int n = s.size();
        unordered_map<string, int> freq;

        for (int i = 0; i < n; i++) {
            string currString = "";

            for (int j = i; j < n; j++) {
                if (currString.empty() || currString.back() == s[j]) {
                    currString += s[j];
                    freq[currString]++;
                } else {
                    break;
                }
            }
        }

        int result = 0;

        for (auto item : freq) {
            string key = item.first;
            int value = item.second;

            if (value >= 3 && key.size() > result)
                result = key.size();
        }
        return result == 0 ? -1 : result;
    }
};