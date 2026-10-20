class Solution {
public:
    int longestSubstring(string s, int k) {
        int n = s.size();
        unordered_map<char, int> freq;

        for (char ch : s)
            freq[ch]++;

        for (int i = 0; i < s.size(); i++) {
            if (freq[s[i]] < k) {
                // this char will not be in answer (since its freq is less than
                // k) answer should be on its left or on its right

                int leftSideArray = longestSubstring(s.substr(0, i), k);
                int rightSideArray =
                    longestSubstring(s.substr(i + 1, n - i + 1), k);

                return max(leftSideArray, rightSideArray);
            }
        }
        return n;
    }
};