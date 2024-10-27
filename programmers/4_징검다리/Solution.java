import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


class Solution {
    /* Point (이분 탐색)
    * 시작점, 바위들, 도착점을 대상으로 가능한 간격들을 저장한 후,
    * 바위 간격의 최소값을 이분 탐색을 통하여 진행하면서, 각각의 단계에서 모든 간격들에 대해 처음 간격부터 하나씩 더해가며,
    * 현재 단계의 최소 값을 넘으면, 다시 처음부터 더해주는 식으로 진행하며 cnt를 업데이트 시켜준다.
    * 이후 cnt가 n(제거할 바위 개수)를 넘으면 현재 단계에 해당하는 최소값은 불가능하단 것이므로, 탐색범위의 끝을 바꿔주고,
    * n보다 같거나 작다면, 더 큰 최소 값이 있을 수 있으므로 시작의 위치를 변경해준다.
    * */
    public int solution(int distance, int[] rocks, int n) {
        int answer = 0;

        Arrays.sort(rocks);
        List<Integer> intervals=new ArrayList<>();

        intervals.add(rocks[0]);// 간격을 구하기 위하여 바위들의 위치를 정렬.
        for (int i = 1; i < rocks.length; i++)intervals.add(rocks[i]-rocks[i-1]);
        intervals.add(distance-rocks[rocks.length-1]);

        int start=0,end=distance;

        while (start <= end) {// 간격의 최소 값을 대상으로 이분 탐색을 진행.
            int mid=(start+end)/2;

            int sum=0,cnt=0;
            for (int i = 0; i < intervals.size(); i++) {
                if (sum + intervals.get(i) < mid) {
                    sum+=intervals.get(i);
                    cnt++;
                }
                else sum=0;
            }

            if (cnt > n) {//다음 최소 값을 만족 시키기 위해, cnt가 n보다 더 많이 필요하단 것이므로 mid 보다 큰 수 불가능.
                end = mid - 1;
            } else {//가능한 경우이며, 더 큰 최소간격이 있을 수 있기 때문에 mid 보다 큰 수 대상으로 진행.
                start=mid+1;
            }
        }

        answer=end;

        return answer;
    }
}