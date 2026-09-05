class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t_mapping = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in s_to_t_mapping and t[i] not in s_to_t_mapping.values():
                s_to_t_mapping[s[i]] = t[i]
            elif s[i] not in s_to_t_mapping and t[i] in s_to_t_mapping.values():
                return False
            elif s[i] in s_to_t_mapping and s_to_t_mapping[s[i]] == t[i]:
                continue
            else:
                return False
            
        return True