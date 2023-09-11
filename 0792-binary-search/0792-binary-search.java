class Solution {
    public int search(int[] nums, int target) {

       int start=0;
       int end=nums.length-1;

        while(start<=end){
            int mid=start+(end-start)/2; //calculate mid point
            if (nums[mid]==target)
            {     
                return mid;   //return mid index
            }          
            else if (nums[mid]>target)  //target<mid, go left
            {   
                end=mid-1;     // shift the end pointer
            }         
            else if (nums[mid]<target) //target>mid, go right
            {    
                start=mid+1;     // shift the start pointer  
            }
        }
        return -1;
 
        
    }
}