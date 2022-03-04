class Solution {
    public int singleNumber(int[] nums) {
        int check = 0;
        int output = 0;
        
        for(int cur=0;cur<nums.length;cur++){
            for(int i=0;i<nums.length;i++){
                 if(cur != i){
                    if(nums[cur] != nums[i]){
                        check++;
                    }
                }
            }
            if(check==nums.length-1)
                output = nums[cur];
            check=0;
        }
        return output;
    }
}
