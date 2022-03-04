import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        List<Integer> answerList = new ArrayList<Integer>();

        Map<String, Integer> genreMap = new HashMap<String, Integer>();
        Map<Integer, Integer> playMap = new HashMap<Integer, Integer>();

        for(int i=0;i<genres.length;i++){
            if(genreMap.containsKey(genres[i])){
                int value = genreMap.get(genres[i]);
                value = value + plays[i];
                genreMap.put(genres[i], value);
            }
            else{
                genreMap.put(genres[i], plays[i]);
            }
        }

        for(int i=0;i<plays.length;i++){
            playMap.put(i, plays[i]);
        }

        List<Map.Entry<String, Integer>> genreEntrySort = new ArrayList<>(genreMap.entrySet());
        List<Map.Entry<Integer, Integer>> playEntrySort = new ArrayList<>(playMap.entrySet());

        Collections.sort(genreEntrySort, new Comparator<Map.Entry<String, Integer>>(){
            @Override
            public int compare(Map.Entry<String, Integer> o1, Map.Entry<String, Integer> o2){
                return o2.getValue().compareTo(o1.getValue());
            }
        });

        Collections.sort(playEntrySort, new Comparator<Map.Entry<Integer, Integer>>(){
            @Override
            public int compare(Map.Entry<Integer, Integer> o1, Map.Entry<Integer, Integer> o2){
                return o2.getValue().compareTo(o1.getValue());
            }
        });

        for(Map.Entry<String, Integer> entryGenre : genreEntrySort){
             int count=0;
            for(Map.Entry<Integer, Integer> entryPlay : playEntrySort){
                if(genres[entryPlay.getKey()].equals(entryGenre.getKey())){
                    answerList.add(entryPlay.getKey());
                    count++;

                    if(count==2){
                        break;
                    }
                }
            }
        }

        int[] answer = new int[answerList.size()];

        for (int i = 0; i < answerList.size(); i++) {
            answer[i] = answerList.get(i);
        }


        return answer;
    }
}
