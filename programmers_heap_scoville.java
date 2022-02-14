import java.util.PriorityQueue;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        
        for(int i : scoville){
            minHeap.add(i);
        }
        
        while(minHeap.size()>=2 && minHeap.peek()<K){
            int lowest = minHeap.poll();
            int secondLowest = minHeap.poll();
            
            int newItem = lowest+ secondLowest*2;
            minHeap.add(newItem);
            answer++;
        }
        if(minHeap.peek()<K){
            answer = -1;
        }
        
        return answer;
    }
}
