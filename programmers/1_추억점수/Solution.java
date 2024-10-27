import java.util.HashMap;
import java.util.Map;

class Solution {

    /* Point (단순 구현)
    * 그리운 사람들의 이름과 그 이름에 해당 하는 점수를 Map을 이용하여 저장한 후, 반복문을 통하여 각각의 사진에 있는 사람들의 점수를 계산하면 된다.
    * 이때 Map에 없는 사람이 사진에 있을 수 있으므로 먼저 있는 사람인지 체크해 주도록 한다.
    * */

    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        int[] answer = {};

        Map<String,Integer> scores=new HashMap<>();

        for (int i = 0; i < name.length; i++)scores.put(name[i],yearning[i]);

        answer=new int[photo.length];

        int idx=0;
        for (int i = 0; i < photo.length; i++) {
            int sum=0;
            for (int j = 0; j < photo[i].length; j++)if(scores.containsKey(photo[i][j]))sum+=scores.get(photo[i][j]);
            answer[idx++]=sum;
        }

        return answer;
    }
}