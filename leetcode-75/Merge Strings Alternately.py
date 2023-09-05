# 1768 Merge Strings Alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1), len(word2))

        new_word = ''
        for i in range(0, min_len):
            new_word += word1[i] + word2[i]

        if len(word1) > len(word2):
            new_word += ''.join(word1[min_len:])

        elif len(word1) < len(word2):
            new_word += ''.join(word2[min_len:])

        return new_word


if __name__ == "__main__":
    a = Solution().mergeAlternately(word1='abc', word2='pqrkl')
    print(a)
