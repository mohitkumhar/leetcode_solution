class Solution {
public:
    bool check(string word, unordered_set<string>& elements,
               map<string, bool>& memo) {
        int n = word.size();

        if (elements.find(word) != elements.end())
            return true;

        if (memo.find(word) != memo.end())
            return memo[word];

        for (int i = 0; i < n - 1; i++) {
            string prefix = word.substr(0, i + 1);
            string suffix = word.substr(i + 1);

            if (check(prefix, elements, memo) &&
                check(suffix, elements, memo)) {
                memo[word] = true;
                return true;
            }
        }
        memo[word] = false;
        return false;
    }

    vector<string> findAllConcatenatedWordsInADict(vector<string>& words) {

        unordered_set<string> elements(words.begin(), words.end());
        vector<string> result;

        for (string word : words) {
            int n = word.size();
            map<string, bool> memo;

            elements.erase(word);
            for (int i = 0; i < n - 1; i++) {
                string prefix = word.substr(0, i + 1);
                string suffix = word.substr(i + 1);

                if (check(prefix, elements, memo) &&
                    check(suffix, elements, memo)) {
                    result.push_back(word);
                    break;
                }
            }
            elements.insert(word);
        }

        return result;
    }
};