class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #XOR as 4^4=0 and 3^0=3
        ans=0
        for i in range(len(nums)):
             ans=ans ^ nums[i]
        return ans

        