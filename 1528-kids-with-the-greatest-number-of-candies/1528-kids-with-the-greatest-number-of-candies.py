class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        #finding maximum from candies
        maxx=max(candies)

        # A list to store result
        result=[]

        for i,candy in enumerate(candies):

            #Comparing each value with maxx
            if candies[i]+extraCandies>=maxx:
                result.append(True) 
            else:
                result.append(False)
                
        return result