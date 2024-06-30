import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    /* Point (그리디 활용)
    * 명함을 긴쪽의 긴쪽들과 짧은 쪽들을 분류해서 저장해서 각각의 최대값을 곱해주면 정답을 구할 수 있다.
    * 왜냐하면 한 명함의 긴쪽과 다른 한 명함의 짧은 쪽을 같은 방향(가로,세로)으로 반영하여 최소 길이를 구하게 된다면, 손해를 볼 수 있다고 판단했기 때문이다.
    * */
    public int solution(int[][] sizes) {
        int answer = 0;

        List<Integer> max=new ArrayList<>();
        List<Integer> min=new ArrayList<>();

        for (int i = 0; i < sizes.length; i++) {
            max.add(sizes[i][0] > sizes[i][1] ? sizes[i][0]:sizes[i][1]);
            min.add(sizes[i][0]> sizes[i][1] ? sizes[i][1] : sizes[i][0]);
        }

        Collections.sort(max,Collections.reverseOrder());
        Collections.sort(min,Collections.reverseOrder());

        answer=max.get(0)*min.get(0);

        return answer;
    }
}