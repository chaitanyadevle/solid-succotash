# 1071. Greatest Common Divisor of Strings
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd_str1 = self.get_gcd_element(str1)
        print('gcd_str1', gcd_str1)
        gcd_str2 = self.get_gcd_element(str2)
        print('gcd_str2', gcd_str2)
        if gcd_str1 == gcd_str2:
            return gcd_str1
        return ''

    def get_gcd_element(self, strs: str):
        prev_x_str = ''
        x_str = ''
        max_count = 0
        for char in strs:
            prev_x_str = x_str
            x_str += char
            count = strs.count(x_str)
            if max_count <= count:
                max_count = count
            else:
                return prev_x_str
        return x_str


if __name__ == "__main__":
    a = Solution().gcdOfStrings(str1='ABABABAB', str2='ABAB')
    print(a)
