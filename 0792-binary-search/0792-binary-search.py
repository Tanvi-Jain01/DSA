class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start=0  #initiaizing start point
        end=len(nums)-1  #initializing end point

        while start<=end:
            mid=start+(end-start)//2   #calculating mid point
            if nums[mid]==target:      #BINGO!
                return mid             #return mid index
            elif nums[mid]>target:     #target<mid, go left
                end=mid-1              # shift the end pointer
            elif nums[mid]<target:     #target>mid, go right
                start=mid+1            # shift the start pointer
        return -1                       #NOT Found
        

        