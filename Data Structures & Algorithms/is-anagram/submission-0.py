class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_s = {}
        for char_s in s:
            freq_s[char_s] = freq_s.get(char_s, 0) + 1

        freq_t = {}
        for char_t in t:
            freq_t[char_t] = freq_t.get(char_t, 0) + 1

        return freq_s == freq_t