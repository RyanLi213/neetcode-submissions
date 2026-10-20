class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_s = dict()
        word_t = dict()
        for i in s:
            if i in word_s:
                word_s[i] += 1 
            else:
                word_s[i] = 0
        for j in t:
            if j in word_t:
                word_t[j] += 1
            else:
                word_t[j] = 0
        if word_s == word_t:
            return True
        else:
            return False