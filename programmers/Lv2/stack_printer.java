import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        
        Queue<Integer> queue = new LinkedList<>();
        Map<Integer, Integer> map = new HashMap<>();
        
        for(int i =0;i<priorities.length;i++){
            queue.add(i);
            map.put(i, priorities[i]);
            
        }
        
        boolean check = false;
        while(true){
            
            for(int i : map.keySet()){
                if(priorities[queue.peek()]<map.get(i)){
                    check=true;
                    break;
                }
            }
            
            if(check==true){
                int value = queue.poll();
                queue.add(value);
            }
            else{
                int index = queue.poll();
                answer++;
                map.remove(index);
                
                if(index==location){
                    break;
                }
            }
            check=false;
        }
        
        return answer;
    }
}
