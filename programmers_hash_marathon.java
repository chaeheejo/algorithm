import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> answerMap = new HashMap<>();
        
        for(String s : completion){
            if(!answerMap.containsKey(s)){
                answerMap.put(s,1);
            }
            else{
                int value = answerMap.get(s);
                value++;
                answerMap.put(s,value);
            }
        }
        
        for(String s : participant){
            if(answerMap.containsKey(s) && answerMap.get(s)>0){
                int value = answerMap.get(s);
                value--;
                answerMap.put(s, value);
            }
            else{
                answer = answer + s;
            }
        }
        
        return answer;
    }
}
