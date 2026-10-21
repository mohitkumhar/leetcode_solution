class Solution {
public:
    int equalSubstring(string s, string t, int maxCost) {
        vector<int> diffArray;
        int n = s.size();

        for (int i = 0; i < n; i++) {
            int diff = abs(s[i] - t[i]);
            diffArray.push_back(diff);
        }

        int i = 0;
        int j = 0;
        int currCost = 0;
        int ans = 0;

        while (j < n) {
            currCost += diffArray[j];

            while (currCost > maxCost) {
                currCost -= diffArray[i];
                i++;
            }
            ans = max(ans, j - i + 1);
            j++;
        }
        return ans;
    }
};