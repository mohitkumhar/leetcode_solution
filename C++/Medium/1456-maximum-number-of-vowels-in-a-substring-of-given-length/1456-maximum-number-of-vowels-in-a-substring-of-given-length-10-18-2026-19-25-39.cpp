class Solution {
public:
    int maxVowels(string s, int k) {
        unordered_set<char> vowel = {'a', 'e', 'i', 'o', 'u'};
        int i = 0;
        int j = 0;

        int n = s.size();
        int currVowelCount = 0;
        int ans = 0;

        while (j < n) {
            if (vowel.find(s[j]) != vowel.end()) {
                currVowelCount += 1;
                ans = max(ans, currVowelCount);
            }

            if (j - i + 1 < k)
                j++;

            else if (j - i + 1 == k) {
                if (vowel.find(s[i]) != vowel.end())
                    currVowelCount--;
                i++;
                j++;
            }
        }
        return ans;
    }
};