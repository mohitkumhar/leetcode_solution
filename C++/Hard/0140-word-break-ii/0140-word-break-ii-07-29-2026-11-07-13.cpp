class Solution {
public:
    vector<string> result;
    void backtrack(int start, vector<string>& currWord, string s,
                   unordered_set<string>& wordDict) {

        if (start >= s.size()) {
            string sentence;
            for (int i = 0; i < currWord.size(); i++) {
                if (i > 0)
                    sentence += " ";
                sentence += currWord[i];
            }

            result.push_back(sentence);
            return;
        }

        for (int j = start; j < s.size(); j++) {
            if (wordDict.find(s.substr(start, j - start + 1)) !=
                wordDict.end()) {
                currWord.push_back(s.substr(start, j - start + 1));
                backtrack(j + 1, currWord, s, wordDict);
                currWord.pop_back();
            }
        }
    }

    vector<string> wordBreak(string s, vector<string>& wordDict) {

        vector<string> currWord;
        unordered_set<string> wordD(wordDict.begin(), wordDict.end());

        backtrack(0, currWord, s, wordD);

        return result;
    }
};