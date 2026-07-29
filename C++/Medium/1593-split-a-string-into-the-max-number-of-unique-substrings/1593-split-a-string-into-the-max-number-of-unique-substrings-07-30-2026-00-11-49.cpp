class Solution {
public:
    int count = 0;

    void backtrack(int i, unordered_set<string>& seen, string s) {
        if (i >= s.size()) {
            count = max(count, static_cast<int>(seen.size()));
            return;
        }

        for (int j = i; j < s.size(); j++) {
            if (seen.find(s.substr(i, j - i + 1)) == seen.end()) {
                seen.insert(s.substr(i, j - i + 1));
                backtrack(j + 1, seen, s);
                seen.erase(s.substr(i, j - i + 1));
            }
        }
    }

    int maxUniqueSplit(string s) {
        int n = s.size();

        unordered_set<string> seen;

        backtrack(0, seen, s);

        return count;
    }
};