class Solution {
    public int majorityElement(int[] nums) {
        int curValue=0;
        
        for(int cur=0;cur<nums.length;cur++){
            curValue=0;
            
            for(int i=0;i<nums.length;i++){
                if(nums[cur]==nums[i]){
                    curValue++;
                }
            }
            
            if(curValue > (nums.length/2)){
                return nums[cur];
            }
        }
        return -1;
    }
}
