# 1431. Kids With the Greatest Number of Candies
from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        x = max(candies)
        is_max_candies = []
        for item in candies:
            if item + extraCandies >= x:
                is_max_candies.append(True)
            else:
                is_max_candies.append(False)
        return is_max_candies

if __name__ == "__main__":
    a = Solution().kidsWithCandies(candies=[1,23,45,44,12], extraCandies=100)
    print(a)
