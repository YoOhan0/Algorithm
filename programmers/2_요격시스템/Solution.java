import java.util.Arrays;

class Solution {
    /* Point (정렬 활용)
    * 시작구간을 오름차순으로 정렬하고, 같다면 도착구간을 오름차순으로 정렬한다.
    * 어느 하나의 구간이라도 하나의 요격은 필요하므로, 앞의 구간부터 최소한 정수 1이상의 구간은 곂치도록 곂치는 구간 정보를 유지 및 업데이트 시키면서 찾고,
    * 더 이상 안 찾아진다면, answer++ 해준 뒤, 다음 구간을 시작으로 똑같은 과정을 반복해주면 최소 유도 미사일 개수를 구할 수 있다.
    * */
    public int solution(int[][] targets) {
        int answer = 0;

        Integer[][] bucket = new Integer[targets.length][targets[0].length];//정렬이 필요하므로 2차원 Wrapper 배열 만들기.
        for(int i=0;i<bucket.length;i++)for(int j=0;j<bucket[i].length;j++)bucket[i][j]=targets[i][j];

        Arrays.sort(bucket,(o1,o2)->{return o1[0]!=o2[0] ? o1[0]-o2[0] : o1[1]-o2[1];});

        int min=bucket[0][0];//첫번째 구간 기준 곂치는 구간 설정.
        int max=bucket[0][1];
        answer++;

        for (int i = 0; i < bucket.length; i++) {

            if (bucket[i][0] < max) {
                min=bucket[i][0];
                max=bucket[i][1] > max ? max : bucket[i][1];

            } else {
                min=bucket[i][0];
                max=bucket[i][1];
                answer++;
            }
        }


        return answer;
    }
}