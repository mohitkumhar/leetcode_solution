class Solution {
public:
    vector<int> findAnagrams(string s, string p) {

        vector<int> result;
        unordered_map<char, int> counter;

        for (char ch : p) {
            counter[ch]++;
        }

        int i = 0;
        int j = 0;

        int n = s.size();
        int k = p.size();

        while (j < n) {
            if (p.find(s[j]) != string::npos) {
                counter[s[j]]--;
                if (counter[s[j]] == 0)
                    counter.erase(s[j]);
            }
            if (j - i + 1 < k)
                j++;

            else if (j - i + 1 == k) {
                if (counter.empty())
                    result.push_back(i);

                if (p.find(s[i]) != string::npos) {
                    counter[s[i]]++;
                    if (counter[s[i]] == 0)
                        counter.erase(s[i]);
                }
                j++;
                i++;
            }
        }
        return result;
    }
};