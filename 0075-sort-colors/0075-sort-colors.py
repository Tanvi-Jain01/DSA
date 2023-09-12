class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Dutch Flag Algorithm

        n=len(nums)
        low=0
        high=n-1
        i=0

        while i<=high:

            if nums[i]==0:
                nums[i],nums[low]=nums[low],nums[i]
                low+=1
              

            elif nums[i]==2:
                 nums[i],nums[high]=nums[high],nums[i]
                 high-=1
                 i-=1
            i+=1
               
           


    


        