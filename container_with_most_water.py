from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Brute Force
        # len_h = len(height)
        # res = 0
        # for h in range(len_h):
        #     for j in range(h + 1, len_h):
        #         area = (j - h) * min(height[h], height[j])
        #         res = max(res, area)
        # return res

        # O(n) linear soln
        l = 0
        r = len(height) - 1
        res = 0

        while l < r:
            area = (r-l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res

if __name__ == "__main__":
    a = Solution().maxArea([1,2])
    print(a)
"""
Input >> List
[1,8,6,2,5,4,8,3,7]
[1,8,6,2,5,4,8,3,7,11,2,3,43,43,45,4]
[4,4,11,4]
"""
