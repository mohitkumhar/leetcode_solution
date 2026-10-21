class Solution {
public:
    bool isAnagram(string s, string t) {

        unordered_map<char, int> freq;

        for (char ch : s) {
            freq[ch]++;
        }

        for (char ch : t) {
            freq[ch]--;
            if (freq[ch] == 0)
                freq.erase(ch);
        }

        return freq.size() == 0;
    }
};