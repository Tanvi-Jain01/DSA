class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos=0
        neg=0
        n=len(nums)

        if nums[-1]<0:
            return n # if last element is <0 then all are negative hence return len of List   O(1)

        
        for i in range(n):
            if nums[i]>0:
                pos+=1  #increment pos if >0
            elif nums[i]<0:
                neg+=1 #increment neg if <0

        return max(pos,neg)   # O(N)
        
        #we can try binary search also to make it logn