# 1768 Merge Strings Alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        smaller = None
        bigger = None
        w1_len = len(word1)
        w2_len = len(word2)
        if w1_len >= w2_len:
            bigger = word1
            smaller= word2
        elif w1_len < w2_len:
            bigger = word2
            smaller= word1

        new_word = ''
        for i in range(len(smaller)):
            new_word += word1[i]
            new_word += word2[i]
        extension = bigger[len(smaller): ]
        new_word += extension
        return new_word

if __name__ == "__main__":
    a = Solution().mergeAlternately(word1='abcde', word2='pqr')
    print(a)
