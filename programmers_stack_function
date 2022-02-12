import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answerList = new ArrayList<Integer>();
        Stack<Integer> stack = new Stack<>();
        
        for(int i=progresses.length-1;i>=0;i--){
            int value = (100-progresses[i])/speeds[i];
            
            if((100-progresses[i])%speeds[i] !=0){
                value++;
            }
            
            stack.push(value);
        }
        
        int value = stack.pop();
        int num =1;
        while(!stack.empty()){
            if(stack.peek()<=value){
                stack.pop();
                num++;
            }
            else{
                answerList.add(num);
                value=stack.pop();
                num=1;
            }
        }
        answerList.add(num);
        
        int[] answer = new int[answerList.size()];

        for (int i = 0; i < answerList.size(); i++) {
            answer[i] = answerList.get(i);
        }
        
        return answer;
    }
}
