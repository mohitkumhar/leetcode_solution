class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        int n = fruits.size();

        int i = 0;
        int j = 0;

        int count = 0;
        int ans = 0;

        unordered_map<int, int> freq;

        while (j < n) {
            if (freq.find(fruits[j]) == freq.end())
                count++;

            freq[fruits[j]]++;

            while (count > 2) {
                freq[fruits[i]]--;
                if (freq[fruits[i]] == 0) {
                    freq.erase(fruits[i]);
                    count--;
                }
                i++;
            }
            ans = max(ans, j - i + 1);
            j++;
        }
        return ans;
    }
};