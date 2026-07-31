class Solution {
public:
    int minimumPushes(string word) {
        unordered_map<int, int> freq;

        int assign_key = 2;
        int ans = 0;

        for (char c : word) {
            freq[assign_key]++;
            ans += freq[assign_key];

            if (assign_key == 9)
                assign_key = 2;
            else
                assign_key++;
        }
        return ans;
    }
};