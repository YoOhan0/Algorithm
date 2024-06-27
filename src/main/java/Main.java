import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {

    public static void main(String[] args) throws IOException {

        System.out.println(solution(25, new int[]{2, 14, 11, 21, 17}, 2));
    }
    static public int solution(int distance, int[] rocks, int n) {
        int answer = 0;

        Arrays.sort(rocks);
        List<Integer> intervals=new ArrayList<>();

        intervals.add(rocks[0]);
        for (int i = 1; i < rocks.length; i++)intervals.add(rocks[i]-rocks[i-1]);
        intervals.add(distance-rocks[rocks.length-1]);

        int start=0,end=distance;

        while (start <= end) {
            int mid=(start+end)/2;

            int sum=0,cnt=0;
            for (int i = 0; i < intervals.size(); i++) {
                if (sum + intervals.get(i) < mid) {
                    sum+=intervals.get(i);
                    cnt++;
                }
                else sum=0;
            }

            if (cnt > n) {
                end = mid - 1;
            } else {
                start=mid+1;
            }
        }

        answer=end;



        return answer;
    }

}
