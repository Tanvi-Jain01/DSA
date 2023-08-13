class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        new_nums=[]
        
#METHOD-1
        count=0  #maintains count of unique elements

        if(n==1):
            return n

        if(n>1):
            new_nums = [nums[0]]
            for i in range(1,n):
                if(nums[i]!=nums[i-1]):
                    new_nums.append(nums[i])  
                    print(new_nums)
                    count+=1
        nums[:]=new_nums
        #return nums


#METHOD-2

        # j=0 #maintains index
        # count=0 #KEEPS COUNT OF UNIQUE ELEMENTS

        # for i in range(1,n): 
        #         if (nums[i]!=nums[i-1]):
        #         # new_nums.append(nums[i])
        #             nums[j+1]=nums[i]
        #             j=j+1
        #             count+=1 
        # del nums[j+1:] 
        # nums= nums[0:j]

       
               
        