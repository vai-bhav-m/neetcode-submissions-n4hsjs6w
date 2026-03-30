class Solution:
    def isValid(self, s: str) -> bool:
        map_dict = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        state = []
        for b in s:
            if b not in map_dict:
                state.append(b)
            else:
                if len(state) == 0:
                    return False
                if state[-1] != map_dict[b]:
                    return False
                else:
                    state.pop()
        if len(state) > 0:
            return False

        return True