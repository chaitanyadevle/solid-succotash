
class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = ('a', 'e', 'i', 'o','u', 'A', 'E', 'I', 'O', 'U')
        vowels_list = []
        for index, value in enumerate(s):
            if value in VOWELS:
                vowels_list.append(value)
        new_s = ''
        for ch in s:
            if ch in VOWELS:
                new_s += vowels_list.pop()
            else:
                new_s += ch
        return new_s


if __name__ == "__main__":
    a = Solution().reverseVowels(s='Revolutionary')
    print(a)
