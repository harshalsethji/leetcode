class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()){
            return "";
        }
        
        std::string prefix = strs[0];
        for (int j = 1; j < strs.size(); j++) {
            std::string current = strs[j];
            int i = 0;
            while (i < prefix.length() && i < current.length() && prefix[i] == current[i]) {
                i++;
            }
            prefix = prefix.substr(0, i);
            if (prefix.empty()){
                return "";
            }
        }
        return prefix;
    }
};
