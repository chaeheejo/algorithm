import java.util.HashMap;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        
        HashMap<String, Integer> clothesMap = new HashMap<>();
        
        for(int i=0;i<clothes.length;i++){
            if(!clothesMap.containsKey(clothes[i][1])){
                clothesMap.put(clothes[i][1], 2);
            }
            else{
                int value = clothesMap.get(clothes[i][1]);
                value++;
                clothesMap.put(clothes[i][1], value);
            }
        }
        
        for(String s : clothesMap.keySet()){
            answer = answer*clothesMap.get(s);
        }
        
        return answer-1;
    }
}
