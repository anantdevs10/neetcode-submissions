class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        if len(flowerbed) > 1:
            i = 0
            while (i != len(flowerbed)):
                if flowerbed[i] == 0:
                    prev_empty = (i ==0) or (flowerbed[i-1]==0)
                    next_empty = (i==len(flowerbed)-1) or (flowerbed[i+1] == 0)
                    if prev_empty and next_empty:
                        flowerbed[i] = 1
                        count += 1
                i+=1

            return (count >= n)
        else:
            return (flowerbed.count(0) >= n)