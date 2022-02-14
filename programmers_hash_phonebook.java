import java.util.HashMap;

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        
        HashMap<String,Integer> map = new HashMap<>();
        
        for(String s : phone_book){
            map.put(s, 1);
        }
        
        String search ="";
        for(String s : phone_book){
            for(int i=0;i<s.length();i++){
                search = s.substring(0,i);
                if(map.containsKey(search)){
                    answer = false;
                    return answer;
                }
            }
        }
        
        return answer;
    }
}
