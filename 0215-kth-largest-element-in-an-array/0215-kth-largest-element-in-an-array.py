class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
          
        
        n=len(nums)
       
        if k>=1 and k<=1000000:
            #Bubble Sort but time limit exceeds.
            # for i in range(n):
            #     for j in range(n-i-1):
            #          if nums[j]>=-100000 and nums[j]<=100000:
            #             if(nums[j]>nums[j+1]):
            #                 nums[j],nums[j+1]=nums[j+1],nums[j]
             sorted_nums = sorted(nums, reverse=True)
       



        return sorted_nums[k-1]




