import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        List<Integer> answerList = new ArrayList<Integer>();

        for(int i=0;i<commands.length;i++){
            List<Integer> sortArray = new ArrayList<Integer>();

            for(int j=commands[i][0]-1;j<commands[i][1];j++){
                sortArray.add(array[j]);
            }

            Collections.sort(sortArray);
            answerList.add(sortArray.get(commands[i][2]-1));
        }

        int[] answer = new int[answerList.size()];

        for (int i = 0; i < answerList.size(); i++) {
            answer[i] = answerList.get(i);
        }

        return answer;
    }
}
