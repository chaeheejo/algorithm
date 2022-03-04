import java.util.*;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        Integer[] citationsSort = new Integer[citations.length];
        
        for(int i =0;i<citations.length;i++){
            citationsSort[i]=citations[i];
        }
        
        Arrays.sort(citationsSort, Collections.reverseOrder());
        
        for(int i=citationsSort[0];i>=0;i--){
            int numOfH=0;
            for(int j=0;j<citationsSort.length;j++){
                if(citationsSort[j]>=i){
                    numOfH++;
                }
                else{
                    break;
                }
            }
            if(numOfH>=i){
                answer = i;
                break;
            }
        }
        
        return answer;
    }
}
