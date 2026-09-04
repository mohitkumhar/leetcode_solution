class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char, int> freq;

        for (char ch : s)
            freq[ch]++;

        // freq: char
        vector<pair<int, char>> count;

        for (auto& it : freq)
            count.push_back({it.second, it.first});

        sort(count.begin(), count.end(),
             [](auto& a, auto& b) { return a.first > b.first; });

        string ans = "";
        for (auto& it : count) {
            ans.append(it.first, it.second);
        }

        return ans;
    }
};