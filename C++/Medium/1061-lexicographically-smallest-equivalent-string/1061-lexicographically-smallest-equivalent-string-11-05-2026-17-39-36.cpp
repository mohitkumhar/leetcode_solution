class Solution {
public:
    char find(char target, unordered_map<char, char>& parent) {
        if (target == parent[target]) {
            return target;
        } else {
            parent[target] = find(parent[target], parent);
            return parent[target];
        }
    }

    void unionSet(char s1, char s2, unordered_map<char, char>& parent) {
        char aParent = find(s1, parent);
        char bParent = find(s2, parent);

        if (aParent < bParent)
            parent[bParent] = aParent;
        else
            parent[aParent] = bParent;
    }

    string smallestEquivalentString(string s1, string s2, string baseStr) {

        int n = s1.size();
        unordered_map<char, char> parent;

        for (int i = 0; i < 26; i++) {
            char ch = 'a' + i;
            parent[ch] = ch;
        }

        for (int i = 0; i < n; i++) {
            unionSet(s1[i], s2[i], parent);
        }

        string smallestString = "";
        for (char ch : baseStr) {
            char smallerString = find(ch, parent);
            smallestString += smallerString;
        }

        return smallestString;
    }
};