class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> matchdict = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };
        
        if (s.length() % 2 == 1) {
            return false;
        }

        stack<char> st;
        for (char ch : s) {
            if (ch == '(' || ch == '[' || ch == '{') {
                st.push(ch);
            }
            else if (matchdict.count(ch)) {
                if (st.empty() || st.top() != matchdict[ch]) {
                    return false;
                }
                st.pop();
            }
        }
        
        return st.empty();
    }
    };
