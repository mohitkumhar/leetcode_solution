class Solution {
public:
    int minimumPushes(string word) {

        vector<int> map(26, 0);

        for (char c : word)
            map[c - 'a']++;

        sort(map.rbegin(), map.rend());

        int result = 0;

        for (int i = 0; i < 26; i++) {
            int freq = map[i];
            int press = i / 8 + 1;
            result += press * freq;
        }

        return result;
    }
};