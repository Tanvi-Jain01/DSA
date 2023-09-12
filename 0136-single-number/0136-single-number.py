class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=len(nums)

        #Brute Force O(N2), but time limit exceeds.
        # for i in range(n):
        #     found=False
        #     for j in range(n):
        #         if(nums[i]==nums[j] and i!=j):
        #            found=True
        #            break
        #     if not found:
        #         return nums[i]



        nums.sort()
        # Iterate through the sorted array, comparing adjacent elements
        for i in range(0, len(nums), 2):
            # If the current element is not equal to the next element, it's the single element
            if i == len(nums) - 1 or nums[i] != nums[i + 1]:
                return nums[i]

       








              
                

        