class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dict = dict()
        for c in s:
            if c not in char_dict:
                char_dict[c] = 0
            char_dict[c] += 1
        
        for c in t:
            if c not in char_dict:
                return False
            else:
                char_dict[c] -= 1
                if char_dict[c] == 0:
                    del char_dict[c]
        
        if len(char_dict) > 0:
            return False
        return True
            