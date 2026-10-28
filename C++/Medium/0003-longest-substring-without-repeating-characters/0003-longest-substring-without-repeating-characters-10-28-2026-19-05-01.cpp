class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int i = 0;
        int j = 0;
        int n = s.size();

        unordered_set<int> seen;
        int ans = 0;

        while (j < n) {
            while (seen.find(s[j]) != seen.end()) {
                seen.erase(s[i]);
                i++;
            }

            if (seen.find(s[j]) == seen.end()) {
                seen.insert(s[j]);
            }

            ans = max(ans, j - i + 1);
            j++;
        }
        return ans;
    }
};