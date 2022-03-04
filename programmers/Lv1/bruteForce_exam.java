import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] answer = {};
        int[] person1 ={1,2,3,4,5};
        int[] person2 = {2,1,2,3,2,4,2,5};
        int[] person3 = {3,3,1,1,2,2,4,4,5,5};
        
        int index=0;
        int[] num = {0,0,0};
        
        while(index<answers.length){
            if(answers[index]==person1[index%5]){
                num[0]++;
            }
            if(answers[index]==person2[index%8]){
                num[1]++;
            }
            if(answers[index]==person3[index%10]){
                num[2]++;
            }
            index++;
        }
        
        ArrayList<Integer> answerList = new ArrayList<Integer>();
        
        int max=0;
        for(int i : num )  {
            max = Math.max(i,max); 
        }
        
        for(int i=0;i<num.length;i++){
            if(max==num[i]){
                answerList.add(i+1);
            }    
        }
        
        answer = new int[answerList.size()];
        
        for(int i =0; i<answer.length; i++) {
        	answer[i] = answerList.get(i);
        }
        
        return answer;
    }
}
