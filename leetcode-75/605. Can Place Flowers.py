# 605. Can Place Flowers
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        max_flowers_to_be_planted = 0
        bed_len = len(flowerbed) -1
        for i in range(len(flowerbed)):
            if not flowerbed[i]:
                prev = flowerbed[i-1] if i != 0 else 0
                next = flowerbed[i+1] if i != bed_len else 0
                if not prev and not next:
                    flowerbed[i] = 1
                    max_flowers_to_be_planted += 1
        return n <= max_flowers_to_be_planted


if __name__ == "__main__":
    a = Solution().canPlaceFlowers(flowerbed=[1,0,0,0,1,0,0], n=2)
    print(a)
