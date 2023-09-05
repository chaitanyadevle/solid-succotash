class Solution:
    def myAtoi(self, s: str) -> int:
        is_neg: bool = False
        is_sign_decoded: bool = False
        MIN = 2**31 * -1
        MAX = 2**31 -1
        is_num = False
        cache = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9
        }
        num = 0

        for i in s:

            # if (is_sign_decoded or not is_neg) and cache.get(i) is None:
            #     break

            if is_num and cache.get(i) is None:
                break


            if  i == ' ':
                continue
            elif i == '+' or i == '-':
                if is_sign_decoded:
                    break
                if i == '-':
                    is_neg = True
                is_sign_decoded = True

            if not (cache.get(i) is None):
                is_num = True
                num = num * 10 + cache.get(i)

            else:
                break

        if is_neg:
            num *= -1

        if num < MIN:
            return MIN
        if num > MAX:
            return MAX

        return num

if __name__ == "__main__":
    # a = Solution().myAtoi("  +  413")
    a = Solution().myAtoi("   -42")
    print(a)

# sdflkj - 345 dfdlek 566