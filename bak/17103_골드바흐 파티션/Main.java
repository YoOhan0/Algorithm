import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int MAXNUM = 1000000;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;

        boolean[] isPrime = new boolean[MAXNUM + 1];
        for (int i = 2; i <= MAXNUM; i++) isPrime[i] = true;
        for (int i = 2; i <= MAXNUM; i++) if (isPrime[i]) for (int j = 2 * i; j <= MAXNUM; j += i) isPrime[j] = false;

        int T = Integer.parseInt(br.readLine());

        for (int t = 0; t < T; t++) {
            int N=Integer.parseInt(br.readLine());
            int answer=0;
            for (int i = 2; i <= N - 2; i++) {
                if(i>N-i)break;
                else if (isPrime[i] && isPrime[N - i]) {
                    answer++;
                }
            }
            System.out.println(answer);
        }
    }
}