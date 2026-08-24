class Solution {
    public int pivotIndex(int[] nums) {
        int totsum=0;
        int leftsum=0;
        for(int num:nums){
            totsum+=num;
        }
        //leftsum==rightsum
        //rightsum=totsum-leftsum-currentElement
        for(int i=0;i<nums.length;i++){
            if(leftsum==totsum-leftsum-nums[i]){
                return i;
            }
            leftsum+=nums[i];
        }
        return -1;
    }
}