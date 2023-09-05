class Solution:
    def reverse(self, x: int) -> int:
        str_abs_x = str(abs(x))
        y = int(str_abs_x[::-1])
        if x < 0:
            y *= -1
        if -2147483648 <= y <= 2147483647:
            return y
        return 0

if __name__ == "__main__":
    a = Solution().reverse(-214748364)
    print(a)