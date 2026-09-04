class Solution {
public:
    bool isIsomorphic(string s, string t) {
        
    unordered_map<char, char> s_to_t;
    unordered_map<char, char> t_to_s;

    for (int i = 0; i < s.size(); i++)
    {
        if (s_to_t.find(s[i]) != s_to_t.end() && s_to_t[s[i]] != t[i])
            return false;

        if (t_to_s.find(t[i]) != t_to_s.end() && t_to_s[t[i]] != s[i])
            return false;
        
        s_to_t[s[i]] = t[i];
        t_to_s[t[i]] = s[i];

    }
    return true ;
    }
};