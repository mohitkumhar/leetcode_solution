class Solution {
public:
    int balancedString(string s) {
        int i = 0;
        int j = 0;


        int n = s.size();
        int k = n / 4;
        int ans = INT_MAX;

        unordered_map<char, int> freq;

        for (char ch : s) {
            freq[ch]++;
        }

        while (j < n) {
            freq[s[j]]--;

            while (i < n &&
                   freq['Q'] <= k && 
                   freq['W'] <= k && 
                   freq['E'] <= k &&
                   freq['R'] <= k) {

                ans = min(ans, j - i + 1);
                freq[s[i]]++;
                i++;
            }
            j++;
        }
        return ans;
    }
};