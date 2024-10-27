import java.util.*;

class Solution {
    /* Point (dfs 활용)
    * 이 문제는 정확성 뿐만 아니라 효율성 또한 만족시켜야하는 문제이다.
    * 처음에는 열별로 모든 격자점에 대하여 dfs를 각각 수행 했는데 답은 맞았지만, 효율성 테스트를 만족하지 못했다.
    * 그래서 방법을 조금 바꿔보았고, 한번만 dfs를 수행하는 대신 IsVisited[][] 배열을 boolean 대신 int 로 바꾸고 방문한 석유 덩어리마다
    * 다른 visit 번호를 부여하였고, 이를 oilMap을 만들어서 각각의 석유덩어리마다 크기를 저장하였다.
    * 이후 열별로 시추 가능한 석유량을 계산할 때, 각 열에 존재하는 visit번호들을 중복을 제거하여 oilMap에 넣어서 합을 계산하고, 이를 이용해 답을 구할 수 있었다.
    * */
    static int Width,Height,VisitValue;
    static int[][] IsVisited=new int[500][500];
    static int[] dy=new int[]{0,0,1,-1};
    static int[] dx=new int[]{1,-1,0,0};

    public int solution(int[][] land) {
        int answer = 0;

        Height=land.length;
        Width=land[0].length;
        VisitValue=1;

        Map<Integer,Integer> oilMap=new HashMap<>();

        for (int i = 0; i < Height; i++) {
            for (int j = 0; j < Width; j++) {
                if (land[i][j] == 1 && IsVisited[i][j] == 0) {
                    int tmp=dfs(i,j,land);
                    oilMap.put(VisitValue++,tmp);
                }
            }
        }

        for (int i = 0; i < Width; i++) {//열

            Set<Integer> tmpSet=new HashSet<>();
            for (int j = 0; j < Height; j++) {//행
                if(land[j][i]==1)tmpSet.add(IsVisited[j][i]);
            }

            int sum=0;
            List<Integer> bucket=new ArrayList<>(tmpSet);
            for(Integer j: bucket)sum+=oilMap.get(j);

            if(answer<sum)answer=sum;

        }

        return answer;
    }

    static int dfs(int y, int x,int[][] land) {

        IsVisited[y][x]=VisitValue;
        int sum=0;
        for (int i = 0; i < 4; i++) {
            int nextY=y+dy[i];
            int nextX=x+dx[i];

            if (isIn(nextY, nextX) &&land[nextY][nextX]==1&& IsVisited[nextY][nextX]==0) {
                sum+=dfs(nextY,nextX,land);
            }
        }

        return 1+sum;
    }
    static boolean isIn(int y,int x) {
        if((y>=0)&&(y<Height)&&(x>=0)&&(x<Width))return true;
        else return false;
    }
}