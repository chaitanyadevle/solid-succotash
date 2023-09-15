class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split(" ")
        print(word_list)
        out_s = ''
        for i in word_list[::-1]:
            if i:
                out_s += i + ' '
        return out_s.strip()


if __name__ == "__main__":
    a = Solution().reverseWords(s='"      hello     world     "')
    print(a)
