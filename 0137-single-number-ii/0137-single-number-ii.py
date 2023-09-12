class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        
        for i in range(0, len(nums), 3):
            # If the current element is not equal to the next element, it's the single element
            if i == len(nums) - 1 or nums[i] != nums[i + 1]:
                return nums[i]