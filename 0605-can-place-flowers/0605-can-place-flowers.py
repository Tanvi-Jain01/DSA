class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        #count the num of zeroes
        zero=flowerbed.count(0)

        #view the testcases and write it in simple manner
        for i in range(len(flowerbed)):
            if n==0:
                return True

            if len(flowerbed)==1 and flowerbed[i]==0 and n==1:
                return True

        #check first position
            if i==0:
                if flowerbed[i]==0 and flowerbed[i+1]!=1:
                    flowerbed[i]=1
                    n-=1

        #check last position
            if i==len(flowerbed)-1:
                if flowerbed[i]==0 and flowerbed[i-1]==0:
                    flowerbed[i]=1
                    n-=1
            #IMP
            if flowerbed[i]==1:
                continue

            else:
                if flowerbed[i-1]==0 and flowerbed[i+1]==0:
                    flowerbed[i]=1
                    n-=1
        
        if n==0:
            return True
        else:
            return False

        
