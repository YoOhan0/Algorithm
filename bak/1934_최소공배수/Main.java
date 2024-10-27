import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int T=Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            st=new StringTokenizer(br.readLine());
            int A=Integer.parseInt(st.nextToken());
            int B=Integer.parseInt(st.nextToken());
            System.out.println(lcm(A,B));
        }
    }
    static int gcd(int a, int b) {
        if(b==0)return a;
        return gcd(b,a%b);
    }
    static int lcm(int a,int b) {
        return a*b/gcd(a,b);
    }
}