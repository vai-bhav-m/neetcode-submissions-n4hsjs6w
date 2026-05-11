class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.size() < 2) return s.size();
        unordered_map<char, int> idx_map;
        int p1 = 0;
        int p2 = 0; 
        int max_size = 1;
        while (p2 < s.size()){
            if (idx_map.count(s[p2]) && idx_map[s[p2]] >= p1) {
                p1 = idx_map[s[p2]] + 1;
            }
            idx_map[s[p2]] = p2;
            max_size = max(p2 - p1 + 1, max_size); // Now safe
            p2++;   
        }
        return max_size;
    }
};
