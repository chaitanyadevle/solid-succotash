class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split()
        out_s = " ".join(word_list[::-1])
        return out_s.strip()


if __name__ == "__main__":
    a = Solution().reverseWords(s='      hello     world     ')
    print(a)
