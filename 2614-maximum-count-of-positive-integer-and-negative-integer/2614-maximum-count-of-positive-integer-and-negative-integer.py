class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos=0
        neg=0
        n=len(nums)

        start=0
        end=n

        if nums[-1]<0 or nums[0]>0:
            return n # if last element is <0 then all are negative hence return len of List   O(1)

        #SOLUTION 1

        # for i in range(n):
        #     if nums[i]>0:
        #         pos+=1  #increment pos if >0
        #     elif nums[i]<0:
        #         neg+=1 #increment neg if <0

        # return max(pos,neg)   # O(N)
        
        #we can try binary search also to make it logn

#!---------------------------------------------------------------
        #SOLUTION-2
       
        mid= start+(end-start)//2
        if nums[mid]<0:
                neg=mid-start+1
                for i in range(mid+1,n):   #O(logn)
                   if nums[i]<0:
                     neg+=1
                    
        else:
            for i in range(n):
                if nums[i]>0:
                    pos+=1  #increment pos if >0
                elif nums[i]<0:
                    neg+=1 #increment neg if <0    O(N)
        
        return max(neg, pos)

          

