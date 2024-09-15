import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static int N,M,BlueY,BlueX,RedY,RedX,DestY,DestX;
    static boolean[][] isObstacle;
    static int[][][][] dp;
    static boolean[][][][] isVisited;
    static int[][] dir=new int[][]{{1,0,0,0,0},{0,1,0,0,1},{0,0,-1,0,0},{0,0,0,-1,1}};//큰 y,큰 x, 작 y, 작 x, 대소 비교 기준(행,열)

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        N=Integer.parseInt(st.nextToken());
        M=Integer.parseInt(st.nextToken());

        isObstacle=new boolean[N][M];

        for (int i = 0; i < N; i++) {
            String str=br.readLine();
            for (int j = 0; j < M; j++) {
                if (str.charAt(j) == '#') {
                    isObstacle[i][j]=true;
                } else if (str.charAt(j) == '.') {
                    isObstacle[i][j]=false;
                } else if (str.charAt(j) == 'O') {
                    DestY=i;
                    DestX=j;
                } else if (str.charAt(j) == 'R') {
                    RedY=i;
                    RedX=j;
                } else if (str.charAt(j) == 'B') {
                    BlueY=i;
                    BlueX=j;
                }
            }
        }
        dp=new int[N][M][4][2];
        isVisited=new boolean[N][M][N][M];

        for (int i = 1; i < N - 1; i++) {
            for (int j = 1; j < M - 1; j++) {
                if (isObstacle[i - 1][j]) dp[i][j][0] = new int[]{i, j};//위 방향
                else dp[i][j][0] = dp[i - 1][j][0];

                if (isObstacle[i][j - 1]) dp[i][j][1] = new int[]{i, j};//왼쪽 방향
                else dp[i][j][1] = dp[i][j - 1][1];

                if (isObstacle[N - 1 - i + 1][j]) dp[N - 1 - i][j][2] = new int[]{N - 1 - i, j};//아래 방향
                else dp[N - 1 - i][j][2] = dp[N - 1 - i + 1][j][2];

                if (isObstacle[i][M - 1 - j + 1]) dp[i][M - 1 - j][3] = new int[]{i, M - 1 - j};//오른쪽 방향
                else dp[i][M - 1 - j][3] = dp[i][M - 1 - j + 1][3];
            }
        }

        Queue<int[]> que=new LinkedList<>();
        que.add(new int[]{RedY,RedX,BlueY,BlueX,0});//시작 구슬들의 위치
        while (!que.isEmpty()) {

            int[] cur= que.poll();
            int[] curR=new int[]{cur[0],cur[1]};
            int[] curB=new int[]{cur[2],cur[3]};
            int curCnt=cur[4];
            if(cur[4]>=10)break;

            if(!isVisited[cur[0]][cur[1]][cur[2]][cur[3]])isVisited[cur[0]][cur[1]][cur[2]][cur[3]]=true;
            else continue;//방문여부를 기록하여, 빨강,파랑구슬의 똑같은 위치의 경우는 다시 수행하지 않도록 한다.

            for (int i = 0; i < 4; i++) {

                int[] nextR = dp[curR[0]][curR[1]][i];
                int[] nextB = dp[curB[0]][curB[1]][i];
                if((curR[0]==nextR[0])&&(curR[1]==nextR[1])&&(curB[0]==nextB[0])&&(curB[1]==nextB[1]))continue;//구슬을 기울여도 제 위치인 경우는 수행하지 않도록 한다.

                if (isIn(curB,nextB,DestY,DestX))continue; //파란공이 구멍에 빠지나 확인.
                else if (isIn(curR,nextR,DestY,DestX)) { //빨강공이 구멍에 빠지나 확인.
                    System.out.println(curCnt+1);
                    return;
                }

                int[] tmp = dir[i]; //{1,0,0,0},{0,1,0,0},{0,0,-1,0},{0,0,0,-1} -> {큰 y,큰 x, 작 y, 작 x}(ex.y축 기준으로 큰 구슬에 추가 연산을 해준다.)

                if ((nextR[0] != nextB[0]) || (nextR[1] != nextB[1])) {//방향별로 반복되는 코드를 템플릿화 하고, dir 배열을 활용함. 해당 코드는 구슬이 겹쳤을 때를 고려하는 과정이다.
                    que.add(new int[]{nextR[0], nextR[1], nextB[0], nextB[1], curCnt + 1});
                } else {
                        if (curR[Math.abs(tmp[4])] > curB[Math.abs(tmp[4])])
                            que.add(new int[]{nextR[0] + tmp[0], nextR[1] + tmp[1], nextB[0]+tmp[2], nextB[1]+tmp[3], curCnt + 1});
                        else que.add(new int[]{nextR[0]+tmp[2], nextR[1]+tmp[3], nextB[0] + tmp[0], nextB[1] + tmp[1], curCnt + 1});
                    }
                }
        }
        System.out.println(-1);
    }

    static boolean isIn(int[] a, int[] b, int comY, int comX) {// 구슬의 경로 내에 구멍이 있는지 확인하는 용도.
        if (comY>=Math.min(a[0],b[0])&&(comY<=Math.max(a[0],b[0]))&&comX>=Math.min(a[1],b[1])&&(comX<=Math.max(a[1],b[1])))return true;
        else return false;
    }
}