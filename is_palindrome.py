class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        nums_list: list = []
        nums_len:int = 0
        while x:
            nums_list.append(x%10)
            x = int(x/10)
            nums_len = len(nums_list)

        for i in range(int(nums_len/2)):
            if nums_list[i] != nums_list[(nums_len-1)-i]:
                return False
        return True

if __name__ == "__main__":
    a = Solution().isPalindrome(123454381)
    print(a)

# 121 --> rev 121
# 1221 -> rev 1221
# -ve nos false
'''
Can be done with two methods
1. By type-casting it to string
    then compare first element to last element.
2. By only doing operations on number
    by dividing it by 10 , 100 and so on
    get the list of nums in the list and them compare.
3. Corner cases:
    1. -ve not allowed
    2. if not matching in between no need to go further

 121 = 1, 2, 1
 121 % 1 = 0
 121 % 10 = 1

'''