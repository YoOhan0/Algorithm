import java.io.*;

public class Main {
    static int MAXNUM = 246912;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        boolean[] isPrime = new boolean[MAXNUM + 1];
        for (int i = 2; i <= MAXNUM; i++) isPrime[i] = true;
        for (int i = 2; i <= MAXNUM; i++) if (isPrime[i]) for (int j = 2 * i; j <= MAXNUM; j += i) isPrime[j] = false;

        while (true) {
            int a = Integer.parseInt(br.readLine());
            if(a==0)break;

            int answer=0;
            for(int i=a+1;i<=2*a;i++)if(isPrime[i])answer++;
            System.out.println(answer);
        }
    }
}